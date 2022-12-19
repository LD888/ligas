import csv
import os
from pathlib import Path

with open("countries.csv") as csvfile:
    file = csv.DictReader(csvfile, dialect='excel', delimiter=';')
    for f in file:
        print(f["code"])
        if not os.path.exists(os.path.join("leagues", f["code"])):
            os.mkdir(os.path.join("leagues", f["code"]))


