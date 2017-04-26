#importing from class Room
from .import Room

#creating livingspace class
class LivingSpace(Room):
    def __init__(self, room_name, room_type):
        self.max_number_of_occupants = 4
        #for python 2
        # super(LivingSpace, self).__init__(self, room_name, room_type)
        Room.__init__(self, room_name, room_type)