class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"The train '{self.name}' has {self.seats} seat(s) available.")

    def fareInfo(self):
        print(f"The fare of the train '{self.name}' is Rs. {self.fare} per ticket.")

    def bookTicket(self):
        if self.seats > 0:
            print(f"Your ticket has been booked! Seat number: {self.seats}")
            self.seats -= 1
        else:
            print("Sorry, the train is full. No seats available.")

# Example usage
train1 = Train("Shatabdi Express", 1500, 5)
train1.getStatus()
train1.fareInfo()
train1.bookTicket()
train1.getStatus()
