
#creating livingspace class
from .Room import Room


class LivingSpace(Room):
    def __init__(self, room_name):
        super(LivingSpace,self).__init__(room_name,'living_space')
        #Room.__init__(Room, room_name, 'living_space')
        self.max_number_of_occupants = 4
        self.all_livingspace_occupants = []

