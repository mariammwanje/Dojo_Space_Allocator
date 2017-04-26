#importing from class Room
from .import Room

#creating class office
class Office(Room):
    def __init__(self):
        self.office_list = []
        self.office_occupants = []