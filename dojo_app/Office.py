#importing from class Room
from .Room import Room

#creating class office
class Office(Room):
    def __init__(self, room_name):
        #inheritating from class Room room name and room type
        Room.__init__(Room, room_name, 'office')
        self.max_no_persons = 6
