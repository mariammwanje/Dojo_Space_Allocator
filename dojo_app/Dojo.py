from dojo_app.Fellow import Fellow
from dojo_app.LivingSpace import LivingSpace
from dojo_app.Office import Office
from dojo_app.Staff import Staff


class Dojo:

    #self variable represents the instance of the object itselfThe __init__ method is roughly what represents a constructor in Python. When you call
    # A() Python creates an object for you, and passes it as the first parameter to the

    def __init__(self):
        # a list containing all the room
        self.all_rooms = []
        self.all_persons = []
        self.all_staff = []
        self.all_fellows = []
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
                return ("room_name({}) " + "room_type({}) has been successfully created".format(room_name, room_type))

        else:
            # if it has not be created successfully
            return ("Room not created Successfully")

    def add_person(self, person_name, person_type, wants_accomodation):
        # checking to see if type person_name and person_type are strings
        if isinstance(person_name, str) and isinstance(person_type, str):
            # creating a person  of type staff
            if (person_type == "staff"):
                self.all_staff.append(Staff(person_name))
                # person of type staff has been created successfully using .format() method
                return (person_name + " " + person_type + " has been successfully created")


            elif (person_type == "fellow"):
                # checking person wants to accomodation, if None or No just append to all_persons list
                if wants_accomodation == None or wants_accomodation == "No":

                    self.all_fellows.append(Fellow(person_name, wants_accomodation))

                    return (person_name + person_type + "does not need accomodation" + " has been successfully added")

                # checking if person wants to accomodation, append to all_persons list
                else:
                    self.all_fellows.append(Fellow(person_name, wants_accomodation))
                    return (person_name + person_type + wants_accomodation + "has been successfully added")


            #     # wants_space = "Yes" if args.get("<wants_space>") is "Y" else "No"
            #     #     if wants_space == "No":
            #     #         if args["Staff"]:
            #     #             new_person = Staff(name)
            #     #             self.staff.append(new_person)
            #     #         elif args["Fellow"]:
            #     #             new_person = Fellow(name)
            #     # self.fellows.append(new_person)
            #     else:
            #         # if it has not be created successfully
            #         return ("Person was not created ")
            #
            # # def add_person(self, name, wants_space):
            # #     self.name = name
            # #     if wants_space == "No":
            # #         new_person = Staff(name)
            # #         self.staff.append(new_person)
            # #     elif wants_space == "Yes":
            # #         new_person = Fellow(name)
            # #         self.fellow.append(new_person)
            #
    def print_room(self):
        pass
    def unallocated_rooms(self):
        pass

    def load_state(self):
        pass

    def save_state(self):
        pass
