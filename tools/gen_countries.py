import json

countries = {
"Africa": ["Algeria","Angola","Benin","Botswana","Burkina Faso","Burundi","Cabo Verde","Cameroon","Central African Republic","Chad","Comoros","Congo (Republic)","Congo (DRC)","Cote d'Ivoire","Djibouti","Egypt","Equatorial Guinea","Eritrea","Eswatini","Ethiopia","Gabon","Gambia","Ghana","Guinea","Guinea-Bissau","Kenya","Lesotho","Liberia","Libya","Madagascar","Malawi","Mali","Mauritania","Mauritius","Morocco","Mozambique","Namibia","Niger","Nigeria","Rwanda","Sao Tome and Principe","Senegal","Seychelles","Sierra Leone","Somalia","South Africa","South Sudan","Sudan","Tanzania","Togo","Tunisia","Uganda","Zambia","Zimbabwe"],
"Americas": ["Antigua and Barbuda","Argentina","Bahamas","Barbados","Belize","Bermuda","Bolivia","Brazil","British Virgin Islands","Canada","Cayman Islands","Chile","Colombia","Costa Rica","Cuba","Dominica","Dominican Republic","Ecuador","El Salvador","Grenada","Guatemala","Guyana","Haiti","Honduras","Jamaica","Mexico","Nicaragua","Panama","Paraguay","Peru","Puerto Rico","Saint Kitts and Nevis","Saint Lucia","Saint Vincent and the Grenadines","Suriname","Trinidad and Tobago","Turks and Caicos","United States","Uruguay","Venezuela"],
"Asia-Pacific": ["Afghanistan","Australia","Bangladesh","Bhutan","Brunei","Cambodia","China","Fiji","Hong Kong SAR","India","Indonesia","Japan","Kazakhstan","Kyrgyzstan","Laos","Macau SAR","Malaysia","Maldives","Mongolia","Myanmar","Nepal","New Zealand","North Korea","Pakistan","Papua New Guinea","Philippines","Samoa","Singapore","South Korea","Sri Lanka","Taiwan","Tajikistan","Thailand","Timor-Leste","Turkmenistan","Uzbekistan","Vanuatu","Vietnam"],
"Europe": ["Albania","Andorra","Austria","Belarus","Belgium","Bosnia and Herzegovina","Bulgaria","Croatia","Cyprus","Czech Republic","Denmark","Estonia","Finland","France","Germany","Gibraltar","Greece","Guernsey","Hungary","Iceland","Ireland","Isle of Man","Italy","Jersey","Kosovo","Latvia","Liechtenstein","Lithuania","Luxembourg","Malta","Moldova","Monaco","Montenegro","Netherlands","North Macedonia","Norway","Poland","Portugal","Romania","Russia","San Marino","Serbia","Slovakia","Slovenia","Spain","Sweden","Switzerland","Ukraine","United Kingdom","Vatican City"],
"Middle East": ["Bahrain","Iran","Iraq","Israel","Jordan","Kuwait","Lebanon","Oman","Palestine","Qatar","Saudi Arabia","Syria","Turkiye","United Arab Emirates","Yemen"],
}

def slugify(name):
    return (name.lower()
            .replace("(", "").replace(")", "")
            .replace("'", "").replace(".", "")
            .replace(",", "").replace(" ", "-"))

published = {"united-kingdom"}

out = []
for region, names in countries.items():
    for n in names:
        slug = slugify(n)
        out.append({
            "name": n,
            "slug": slug,
            "region": region,
            "status": "published" if slug in published else "pending"
        })

with open("/home/claude/gtg/data/countries.json", "w") as f:
    json.dump(out, f, indent=2)

print(len(out), "jurisdictions written")
