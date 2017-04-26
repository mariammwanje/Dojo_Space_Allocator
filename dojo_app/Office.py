#importing from class Room
from .import Room

#creating class office
class Office(Room):
    def __init__(self):
        self.max_number = 6
        self.occupants = []