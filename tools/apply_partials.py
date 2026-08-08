"""
tools/apply_partials.py

Single source of truth propagation for Global Tax Guide's header and footer.

HOW THIS WORKS
--------------
partials/header.html and partials/footer.html are the ONLY place the header
and footer markup should ever be edited. Each contains {{HOME}} and/or
{{BASE}} tokens that get substituted per-file depending on how deep the file
sits relative to the repo root:
  - Root-level pages (index.html, about.html, map.html, zones.html,
    unions.html, trusted-resources.html, mission.html, disclaimer.html):
    HOME = "./"   BASE = ""
  - countries/*.html:
    HOME = "../"  BASE = "../"

To change the header or footer sitewide:
  1. Edit partials/header.html or partials/footer.html only.
  2. Run this script.
  3. It rewrites every HTML file's <header class="site-header">...</header>
     and <footer class="site-footer">...</footer> block (plus strips any
     legacy orphan <p class="disclaimer"> that used to sit outside the
     footer on a handful of pages) and pushes everything as ONE atomic git
     tree commit.

This is a deliberate choice over a JS-injected header/footer: the site's
static HTML must be fully readable by crawlers and LLMs that do not execute
JavaScript, so the canonical content has to already be present in the
delivered markup, not injected client-side after page load.
"""
import os, re, json, base64, urllib.request, concurrent.futures

GH_TOKEN = os.environ["GH_TOKEN"]
OWNER = "tk-cpa"
REPO = "globaltaxguide"
API = f"https://api.github.com/repos/{OWNER}/{REPO}"
RAW = f"https://raw.githubusercontent.com/{OWNER}/{REPO}/main"

def _req(method, path, data=None):
    url = f"{API}/{path}"
    headers = {"Authorization": f"token {GH_TOKEN}", "Accept": "application/vnd.github+json", "User-Agent": "gtg-agent"}
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())

def fetch_raw(path):
    req = urllib.request.Request(f"{RAW}/{path}", headers={"User-Agent": "x"})
    with urllib.request.urlopen(req) as resp:
        return resp.read().decode("utf-8")

ROOT_PAGES = [
    "index.html", "about.html", "map.html", "zones.html",
    "unions.html", "trusted-resources.html", "mission.html", "disclaimer.html",
]

HEADER_RE = re.compile(r'<header class="site-header">.*?</header>', re.DOTALL)
FOOTER_RE = re.compile(r'<footer class="site-footer">.*?</footer>(\s*<p class="disclaimer">.*?</p>)?', re.DOTALL)

def render(partial_text, home, base):
    return partial_text.replace("{{HOME}}", home).replace("{{BASE}}", base)

def apply_to_content(content, header_html, footer_html):
    content = HEADER_RE.sub(lambda m: header_html.rstrip("\n"), content, count=1)
    content = FOOTER_RE.sub(lambda m: footer_html.rstrip("\n"), content, count=1)
    return content

def main():
    header_partial = open("partials/header.html", encoding="utf-8").read()
    footer_partial = open("partials/footer.html", encoding="utf-8").read()

    header_root = render(header_partial, "./", "")
    footer_root = render(footer_partial, "./", "")
    header_country = render(header_partial, "../", "../")
    footer_country = render(footer_partial, "../", "../")

    # discover all countries/*.html files
    tree = _req("GET", "git/trees/main?recursive=1")
    country_files = [e["path"] for e in tree["tree"] if e["path"].startswith("countries/") and e["path"].endswith(".html")]

    root_files = [p for p in ROOT_PAGES if p != "disclaimer.html"]  # disclaimer.html pushed fresh, not fetched

    def fetch_and_transform_root(path):
        try:
            c = fetch_raw(path)
        except Exception:
            return None
        new_c = apply_to_content(c, header_root, footer_root)
        return (path, new_c) if new_c != c else None

    def fetch_and_transform_country(path):
        c = fetch_raw(path)
        new_c = apply_to_content(c, header_country, footer_country)
        return (path, new_c) if new_c != c else None

    changed = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=24) as ex:
        for res in ex.map(fetch_and_transform_root, root_files):
            if res:
                changed[res[0]] = res[1]
        for res in ex.map(fetch_and_transform_country, country_files):
            if res:
                changed[res[0]] = res[1]

    # always include disclaimer.html (new page) and the partials + this script + updated CSS
    changed["disclaimer.html"] = open("disclaimer.html", encoding="utf-8").read()
    changed["partials/header.html"] = header_partial
    changed["partials/footer.html"] = footer_partial
    changed["tools/apply_partials.py"] = open("apply_partials.py", encoding="utf-8").read()
    changed["assets/styles.css"] = open("styles.css", encoding="utf-8").read()

    print(f"{len(changed)} files to commit")

    ref = _req("GET", "git/ref/heads/main")
    base_commit_sha = ref["object"]["sha"]
    base_commit = _req("GET", f"git/commits/{base_commit_sha}")
    base_tree_sha = base_commit["tree"]["sha"]

    tree_entries = [
        {"path": path, "mode": "100644", "type": "blob", "content": content}
        for path, content in changed.items()
    ]

    new_tree = _req("POST", "git/trees", {"base_tree": base_tree_sha, "tree": tree_entries})
    new_commit = _req("POST", "git/commits", {
        "message": "Unify header/footer via single-source partials (all pages); add disclaimer.html; restyle footer",
        "tree": new_tree["sha"],
        "parents": [base_commit_sha],
    })
    _req("PATCH", "git/refs/heads/main", {"sha": new_commit["sha"]})
    print("Committed:", new_commit["sha"])

if __name__ == "__main__":
    main()
