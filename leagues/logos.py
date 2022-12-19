import os
from pathlib import Path
from bs4 import BeautifulSoup
import urllib.request

training = {"Poor": "1",
"Basic": "1",
"Below Average": "2",
"Adequate": "2",
"Average": "2",
"Good": "3",
"Great": "3",
"Excellent": "3",
"Superb": "4",
"State of the Art": "4"}

youth_facility = {"Poor": "1",
"Basic": "1",
"Below Average": "2",
"Adequate": "2",
"Average": "2",
"Good": "3",
"Great": "3",
"Excellent": "3",
"Superb": "4",
"State of the Art": "4"}


junior = {"Poor": "1",
"Basic": "1",
"Below Average": "2",
"Adequate": "2",
"Average": "2",
"Good": "3",
"Great": "3",
"Excellent": "3",
"Superb": "4",
"State of the Art": "4"}


youth_recruitmen = {"Limited": "1",
"Basic": "1",
"Fairly Basic": "2",
"Adequate": "2",
"Average": "3",
"Good": "3",
"Excellent": "4",
"Exceptional": "4"}


paths = [f for f in os.listdir('.') if "." not in f ]
files = []
htmls = []
for p in paths:
    if os.listdir(p):
        files = []
        files += [f for f in os.listdir(p) if ".html" in f ]
        htmls += [os.path.join(p, f)for f in files]
        

for i in htmls:
    principal = str(i).split("\\")[0]
    secundario = str(i).split("\\")[1].replace(".html", "")
    archivo = open(i, "r", encoding="utf-8")
    soup = BeautifulSoup(archivo, 'html.parser')
    archivo.close()
    images_src = []
    names = []
    txtt = "name,budge,lvl-stadium,lvl-facilities,lvl-marketing,lvl-medical-center,lvl-team" + "\n"
    for x in soup.find_all("tbody"):
        for y in x.find_all("tr"):
            ddd = y.find_all("td")
            nombre = ddd[1].get_text().strip("\n")
            balance = ddd[2].get_text().replace("£", "").strip("\n").strip()
            facilitylvl = training[ddd[7].get_text().strip("\n")]
            lvlteam = ddd[-2].get_text().strip("\n")              
            print(nombre ,balance , facilitylvl ,facilitylvl , facilitylvl , facilitylvl ,lvlteam )
            txtt += nombre + "," + balance + "," + facilitylvl + "," + facilitylvl + "," + facilitylvl + "," + facilitylvl + "," + lvlteam + "\n"
            
            
    if not os.path.exists(os.path.join(principal, secundario + ".csv")):
        arch = open(os.path.join(principal, secundario + ".csv"), "w")
        arch.write(txtt)
        arch.close()

    for x in soup.find_all("img"):
        images_src.append(x.get("src"))
        
    for x in soup.find_all("a"):
        names.append(x.get_text().strip("\n"))

    for url, name in zip(images_src, names):
        name = name.replace("\'", "-").replace("/", "-")
        if not os.path.exists(os.path.join(principal, secundario)):
            os.mkdir(os.path.join(principal, secundario))
        if not os.path.exists(os.path.join(principal, secundario ,name + ".png")):
            urllib.request.urlretrieve(url, os.path.join(principal, secundario ,name + ".png"))
    

print("END")
