from functions import kubas

s = "Ricardas"

for letter in s:
    print(letter)

a = ["Naujamiestis", "Lazdynai", "Žvėrynas", "Savanoriai"]

for rajonas in a:
    print(rajonas)

baldai = {"kede": "juoda", "sofa": "smeline", "televizorius": "juodas"}
print (baldai["televizorius"])


for i in range (4):
    print(f"{i} kubas yra {kubas(i)}")
