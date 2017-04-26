#importing from class Room
from .import Room

#creating livingspace class
class LivingSpace(Room):
    def __init__(self, room_name, room_type ):
        self.max_number_occ = 4
        self.living_space_list = []
        self.occupants = []