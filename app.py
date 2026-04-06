from parking_management import ParkingManagement
from models.car import Car

pm = ParkingManagement()
pm.create_parking_slots(5)

car1 = Car("TS09AB1234", 25)
slot = pm.issue_parking_ticket("TS09AB1234", 25)

print(f"Allocated Slot: {slot}")
