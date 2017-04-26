# from dojo_app.Fellow import Fellow
from .Fellow import Fellow
from .LivingSpace import LivingSpace
from .Office import Office
# from dojo_app.Staff import Staff
from .Staff import Staff


class Dojo():
    def __init__(self):
        # a list containing all the room
        self.all_rooms = []
        self.all_persons = []
        #self.staff = []
        #self.fellow = []
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
                return ("room_name({}) " + "room_type({}) has been successfully created".format(room_name, room_type ))

        else:
            # if it has not be created successfully
            return ("Room not created Successfully")



    def add_person(self, person_name, person_type):
        # checking to see if type person_name and person_type are strings
        if isinstance(person_name, str) and isinstance(person_type, str):
            # creating a person  of type staff
            if (person_type == "staff"):
                self.all_persons.append(Staff(person_name))
                # person of type staff hashas been created successfully using .format() method
                return (
                "person_name({}) " + "person_type({}) has been successfully created".format(person_name, person_type))

            elif (person_type == "fellow"):
                self.all_persons.append(Fellow(person_name))
                # person of type fellow has been created successfully using .format() method
                return (
                "person_name({}) " + "person_type({}) has been successfully created".format(person_name, person_type))


        else:
            # if it has not be created successfully
            return ("Person was not created ")

    # def add_person(self, name, wants_space):
    #     self.name = name
    #     if wants_space == "No":
    #         new_person = Staff(name)
    #         self.staff.append(new_person)
    #     elif wants_space == "Yes":
    #         new_person = Fellow(name)
    #         self.fellow.append(new_person)

    def allocated_rooms(self):
        pass

    def unallocated_rooms(self):
        pass

    def load_state(self):
        pass

    def save_state(self):
        pass
