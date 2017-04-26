from dojo_app.Room import Room


class Dojo():
    def __init__(self):
        #a list containing all the room
        self.all_rooms = []
        self.room_list = [self.office_list,self.livingspace_list]
        # self.livingspace_list = []
        self.occupants = []


    def create_room(self, room_name, room_type):
        #checking to see if type room_name and room_type are strings
        if isinstance(str, room_name) and isinstance(str, room_type):
            self.all_rooms.append(Room(room_name, room_type))
            #if it has been created successfully using .format() method
            return ("self.room_name({}) and self.room_type({}) has been successfully created".format(room_name,room_type))

        else:
            #if it has not be created successfully
            return ("Room not created Successfully")

    def add_person(self):
        pass
    def allocated_rooms(self):
        pass
    def unallocated_rooms(self):
        pass
    def load_state(self):
        pass
    def save_state(self):
        pass

