import flight_class

f = flight_class.Flight(4)
passengers = ["Rita", "Andrius", "Domas", "Indra", "Aleksas"]

for passenger in passengers:
    if f.add_passenger(passenger):
        print(f"{passenger} will fly!")
    else:
        print(f"{passenger} has no seat left :(")
