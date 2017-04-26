from dojo_app.Fellow import Fellow
from dojo_app.LivingSpace import LivingSpace
from dojo_app.Office import Office
from dojo_app.Staff import Staff


class Dojo():
    def __init__(self):
        # a list containing all the room
        self.all_rooms = []
        self.staff = []
        self.fellow = []
        self.occupants = []

    def create_room(self, room_name, room_type):
        # checking to see if type room_name and room_type are strings
        if isinstance(room_name, str) and isinstance(room_type, str):
            # checking to see if room created is of type office
            # creating a room  of type office

            if (room_type == "office"):
                self.all_rooms.append(Office(room_name))
                # if it has been created successfully using .format() method
                return ("room_name({}) " + "room_type({}) has been successfully created".format(room_name, room_type))

            elif (room_type == "living_space"):
                self.all_rooms.append(LivingSpace(room_name))
                # if it has been created successfully using .format() method
                return ("room_name({}) " + "room_type({}) has been successfully created".format(room_name, room_type, ))

        else:
            # if it has not be created successfully
            return ("Room not created Successfully")

    def add_person(self, name, wants_space):
        self.name = name
        if wants_space == "No":
            new_person = Staff(name)
            self.staff.append(new_person)
        elif wants_space == "Yes":
            new_person = Fellow(name)
            self.fellow.append(new_person)



    def allocated_rooms(self):
        pass

    def unallocated_rooms(self):
        pass

    def load_state(self):
        pass

    def save_state(self):
        pass
