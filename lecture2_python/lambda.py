people = [
    {"vardas": "Rita", "rysys": "ji"},
    {"vardas": "Domas", "rysys": "brolis"},
    {"vardas": "Andrius", "rysys": "brolis"},
    {"vardas": "Indra", "rysys": "sesuo"},
    {"vardas": "Aleksas", "rysys": "sunus"},
]

# def f(person):
#     return person["vardas"]

# people.sort(key=f)

people.sort(key=lambda person: person["vardas"])
print(people)

broliai = list(filter(lambda person: person["rysys"] == "brolis", people))
print(broliai)
