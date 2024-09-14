from classes.parking_slot import ParkingSlot

def add_slot(carpark):
    print ("Adding slot")
    # Take input the id for the parking slot
    slot_id = input("Enter id for the parking slot: ")
    # Create an instance of the parking slot
    parking_slot = ParkingSlot(slot_id)
    # Add the slot to the carpark
    carpark.add_slot(parking_slot)
    print("Parking slot added\n")

def list_slots(carpark):
    all_slots = carpark.get_slots()
    print("\nListing slots..")
    if not all_slots:
        print("No slots available.")
    for slot in all_slots:
        print(slot)
    print("\n")