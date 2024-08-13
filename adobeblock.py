import requests

url = "https://raw.githubusercontent.com/Ruddernation-Designs/Adobe-URL-Block-List/master/PiHole"
response = requests.get(url)
text_lines = response.text.split("\n")
lines = "payload:\n"
for line in text_lines:
    if len(line) == 0:
        continue
    elif line[0] == "#":
        continue
    elif line[-1].isdigit():
        lines = lines+"  - "+line+"\n"
    else:
        lines = lines+"  - DOMAIN-SUFFIX,"+line+"\n"
with open("AdobeBlock.yaml", 'w', encoding='utf-8') as file:
    file.write(lines)
