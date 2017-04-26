#importing from class Room
from .import Room

#creating livingspace class
class LivingSpace(Room):
    def __init__(self):
        self.livingspace_list = []
        self.living_occupants = []