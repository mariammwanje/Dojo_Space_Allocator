
#creating livingspace class
from dojo_app.Room import Room


class LivingSpace(Room):
    def __init__(self, room_name):
        Room.__init__(Room, room_name, 'living_space')
        self.max_number_of_occupants = 4
