from dojo_app import Fellow
from dojo_app import Staff


class Person():

    def __init__(self,person_name,person_type):
        self.person_name = person_name
        self.person_type = person_type


















































    # def add_person(self, name, type, want_accomodation='n'):
    #     '''By default someone needs an Office '''
    #     staf = list(Staff.staff_names)
    #     felo = list(Fellow.fellow_names)
    #     if name in staf or name in felo:
    #         return name + ' already exists'
    #
    #     elif type_person == 'staff':
    #         if 'y' == want_accomodation:
    #             return 'staff cannot have accomodation'
    #
    #         create_staff = self.add(name, type_person)
    #         if create_staff is not True:
    #             return create_staff
    #
    #         # By default the staff should never be allocated living space
    #         allocate_office = self.room.allocate_space(name)
    #         if allocate_office is not True:
    #             return allocate_office
    #         return 'Allocated Office:' + str(self.room.get_room(name))
    #
    #     create_fellow = self.add(name, type_person)
    #     if create_fellow is not True:
    #         return create_fellow
    #
    #     # A fellow may or not want accomodation
    #     return self.room.allocate_space(name, want_accomodation)
    #
    # def add(self, person_name, type_person):
    #     if person_name == '' or type(person_name) != str:
    #         return 'Invalid person name type used'
    #
    #     elif len(person_name) > 21:
    #         return 'Too long person name'
    #
    #     if type_person == 'fellow':
    #         return self.add_one_fellow(person_name)
    #     elif type_person == 'staff':
    #         return self.add_one_staff(person_name)
    #     else:
    #         return " '" + type_person + "' type person is unknown"
    #
    # def get_room_members(self, room_name):
    #     if room_name in list(Office.office_n_occupants.keys()):
    #         return Office.office_n_occupants[room_name]
    #     elif room_name in list(LivingSpace.room_n_occupants.keys()):
    #         return LivingSpace.room_n_occupants[room_name]
    #     return 'Room not Found'
