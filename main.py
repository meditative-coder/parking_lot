import re

class Vehicle:

    # regex to match if any vehicle's registration number is valid or not
    registration_number_format = r"^[A-Z]{2}[-][0-9]{2}[-][A-Z]{1,2}[-][0-9]{4}$"
    def __init__(self, registration_number, color, assigned_slot):
        self.registration_number = registration_number
        self.color = color
        self.assigned_slot = assigned_slot

    @classmethod
    def check_valid_vehicle_number(cls, reg_no):

        p = re.compile(Vehicle.registration_number_format)

        if bool(p.match(reg_no)):
            return True
        return False

    def __str__(self):
        return self.registration_number+" "+self.color+" "+str(self.assigned_slot)

class MultiStoreyParking:
    def __init__(self, capacity):
        self.capacity = capacity
        self.mappings = dict()
        for i in range(capacity):
            self.mappings[i+1] = None


    def get_closest_slot(self):
        for slot, vehicle in self.mappings.items():
            if vehicle == None:
                return slot
        return -1

    def currently_parked_vehicles(self):
        pass

    def park_vehicle(self, vehicle_to_park):
        closest_slot = self.get_closest_slot()
        print("Closest Slot: ", closest_slot)
        if closest_slot != -1:
            self.mappings[closest_slot] = vehicle_to_park
            return "Allocated Slot Number: "+ str(closest_slot)
        else:
            return "Sorry, parking is full"

    def get_vehicle_slot_by_registration_number(self, reg_no):
        is_valid_reg_no = Vehicle.check_valid_vehicle_number(reg_no=reg_no)
        if not is_valid_reg_no:
            return -1
        else:
            for slot, vehicle in self.mappings.items():
                if vehicle.registration_number == reg_no:
                    return slot
            return 0

    def get_vehicle_reg_no_by_color(self, color):
        for value in self.mappings.values():
            if value is not None:
                if value.color == color:
                    yield value.registration_number

    def get_slot_no_by_color(self, color):
        for key, value in self.mappings.items():
            if value is not None:
                if value.color == color:
                    yield key

    def get_status(self):
        print('Slot No. \t Registration No.\tColour')
        for key, value in self.mappings.items():
            if value is not None:
                print(key,"\t\t",value.registration_number,"\t", value.color)

    def exit(self, slot):
        try:
            obj = self.mappings[slot]
            self.mappings[slot] = None
            del obj
            return f"Slot number {slot} is free"
        except KeyError as err:
            return f"Non existent slot: {slot}"

    



if __name__ == "__main__":
    parking = None
    while(True):
        command = input()
        command = command.split()
        if command[0] == "create_parking_lot":
            capacity_of_parking_slot = int(command[1])
            parking = MultiStoreyParking(capacity_of_parking_slot)
            print(f"Created a parking lot with {capacity_of_parking_slot} slots")

        elif command[0] == 'park':
            closest_available_slot = parking.get_closest_slot()
            reg_no = command[1]
            color = command[2]
            is_valid_reg_no = Vehicle.check_valid_vehicle_number(reg_no=reg_no)
            if is_valid_reg_no:
                vehicle = Vehicle(registration_number=reg_no,color=color,assigned_slot=closest_available_slot)
                print(parking.park_vehicle(vehicle_to_park=vehicle))
            else:
                print("Please enter a valid registration number")

        elif command[0] == "leave":
            slot_to_free = int(command[1])
            print(parking.exit(slot = slot_to_free))
        
        elif command[0] == "status":
            parking.get_status()
            
        
        elif command[0] == "registration_numbers_for_cars_with_colour":
            color = command[1]
            for reg_no in parking.get_vehicle_reg_no_by_color(color=color):
                print(reg_no, end="\t")
            print("\n")

        elif command[0] == "slot_numbers_for_cars_with_colour":
            color = command[1]
            for slot in parking.get_slot_no_by_color(color=color):
                print(slot, end="\t")
            print("\n")


        elif command[0] == "slot_number_for_registration_number":
            reg_no = command[1]

            slot = parking.get_vehicle_slot_by_registration_number(reg_no=reg_no)

            if slot==-1:
                print("Please enter a valid registration number")
            elif slot == 0:
                print("Not Found")
            else:
                print(slot)
        
        elif command[0]=="exit":
            break



                

