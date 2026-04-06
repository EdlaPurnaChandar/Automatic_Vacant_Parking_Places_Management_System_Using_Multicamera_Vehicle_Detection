import argparse
import sys
from heapq import heapify, heappush, heappop
from Models.Car import Car
from Models.ParkingTicket import ParkingTicket

class ParkingManagement:
    """
    This is the Main Class for Managing Automated Parking Ticketing System.
    """

    def __init__(self):
        """
        This constructor method is used to initialize the capacity,
        available_parking_slots and occupied_parking_slots parameters.
        """
        self.capacity = 0
        self.available_parking_slots = []
        self.occupied_parking_slots = {}

    def create_parking_slots(self, max_capacity):
        """
        Creates parking slots using min heap.
        """
        try:
            self.capacity = max_capacity
            heapify(self.available_parking_slots)

            for parking_slots_index in range(1, self.capacity + 1):
                heappush(self.available_parking_slots, parking_slots_index)

            return True
        except Exception as exception:
            print(exception)
            return False

    def get_nearest_empty_parking_slot(self):
        """
        Returns nearest available parking slot.
        """
        available_parking_slot = heappop(self.available_parking_slots)
        return available_parking_slot

    def allocate_parking_slot(self, car):
        """
        Allocates nearest parking slot to car.
        """
        if len(self.occupied_parking_slots) < self.capacity:
            parking_slot = self.get_nearest_empty_parking_slot()
            vehicle_registration_number = car.get_registration_number()

            parking_ticket = ParkingTicket(car, parking_slot)

            self.occupied_parking_slots[
                vehicle_registration_number
            ] = parking_ticket
        else:
            parking_slot = -1

        return parking_slot

    def deallocate_parking_slot(self, parking_slot_number):
        """
        Deallocates parking slot when car leaves.
        """
        if len(self.occupied_parking_slots) > 0:
            key = -1

            for vehicle_registration_number, parking_ticket in self.occupied_parking_slots.items():
                if parking_ticket.get_parking_slot() == parking_slot_number:
                    key = vehicle_registration_number
                    value = parking_ticket
                    break

            if key == -1:
                return False
            else:
                del self.occupied_parking_slots[key]
                heappush(self.available_parking_slots, parking_slot_number)
                return value
        else:
            return False

    def issue_parking_ticket(self, vehicle_registration_number, driver_age):
        """
        Issues parking ticket.
        """
        # Create Car object
        car = Car(vehicle_registration_number, driver_age)

        # Allocate parking slot
        parking_slot = self.allocate_parking_slot(car)

        return parking_slot
