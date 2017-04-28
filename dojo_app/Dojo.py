from dojo_app.Fellow import Fellow
from dojo_app.LivingSpace import LivingSpace
from dojo_app.Office import Office
from dojo_app.Staff import Staff


class Dojo:
    # self variable represents the instance of the object itselfThe __init__ method is roughly what represents a constructor in Python. When you call
    # A() Python creates an object for you, and passes it as the first parameter to the

    def __init__(self):
        # a list containing all the room
        self.all_rooms = []
        self.all_persons = []

    def create_room(self, room_type, room_name):
        # checking to see if type room_name and room_type are strings
        if isinstance(room_type, str) and isinstance(room_name, str):
            # checking to see if room created is of type office
            # creating a room  of type office

            if (room_type == "office"):
                self.all_rooms.append(Office(room_name))
                # if it has been created successfully using .format() method
                #return (room_type + room_name + "has been successfully created")
                return True

            elif (room_type == "living_space"):
                self.all_rooms.append(LivingSpace(room_name))
                # if it has been created successfully using .format() method
                #return (room_type + room_name + " has been successfully created")
                return True

        else:
                # if it has not be created successfully
            print("Room not created Successfully")




    def add_person(self, person_type, person_name, wants_accomodation):
        # checking to see if type person_name and person_type are strings
        if isinstance(person_type, str) and isinstance(person_name, str):
            # creating a person  of type staff
            if person_type == "staff":
                self.all_persons.append(Staff(person_name))
                # person of type staff has been created successfully using .format() method
                return True
            elif person_type == "fellow":
                # checking person wants to accomodation, if None or No just append to all_persons list
                if wants_accomodation == None or wants_accomodation == "No":

                    self.all_persons.append(Fellow(person_name, wants_accomodation))

                    return True

                # checking if person wants to accomodation, append to all_persons list
                else:
                    self.all_persons.append(Fellow(person_name, wants_accomodation))
                    return True
        return (False)


if __name__ == "__main__":
    pass
