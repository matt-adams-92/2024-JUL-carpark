class ParkingSlot:
    def __init__(self, id):
        self.id = id
        self.is_occupied = False
        self.car = None
    
    def __str__(self):
        if self.car:
            return f"Parking slot with id {self.id} and has the following car: {self.car}"
        else:
            return f"Parking slot with id {self.id}"