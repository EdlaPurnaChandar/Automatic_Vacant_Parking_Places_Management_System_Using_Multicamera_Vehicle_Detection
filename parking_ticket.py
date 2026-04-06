class ParkingTicket:
    def __init__(self, car, parking_slot):
        self.car = car
        self.parking_slot = parking_slot

    def get_parking_slot(self):
        return self.parking_slot
