class Flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, passenger):
        if not self.empty_seats():
            return False
        else:
            self.passengers.append(passenger)
            return True
    
    def empty_seats(self):
        return self.capacity - len(self.passengers)
        