import unittest

from dojo_app import LivingSpace
from dojo_app import Office
from dojo_app.Dojo import Dojo
from dojo_app.Room import Room



class TestCaseRoom(unittest.TestCase):

    # def setUp(self):
    #     self.andela_dojo_room = Dojo()

#creating aunit test for the create room function
    def test_create_room(self):
        # andela = self.andela_dojo_room.create_room("Orange", "living_space")
        #creating an object andela_dojo from Dojo class
        #andela_dojo.create_room(room_name, room_type)
        #creating a room by using room name ad room type as parameters from create_room function
        andela_dojo = Dojo()

        initial_room_count = len(andela_dojo.all_rooms)
        #creating an object andela_dojo from Dojo class
        blue_office = andela_dojo.create_room('Blue', 'office')
        self.assertTrue(blue_office)
        new_room_count = len(andela_dojo.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)
        # checking that self.all_rooms[0] should be an instance of office.
        # self.assertTrue(isinstance(self.andela_dojo.all_rooms[0], Office))

# # testing to see if LivingSpace inherits from Room
class TestCaseLivingSpace(unittest.TestCase):
    def test_livingspace_inheritence(self):
        # checking is livingspace is a subclass of Room
        self.assertTrue(issubclass(LivingSpace, Room))

# testing to see if Office inherits from Room
class TestCaseOffice(unittest.TestCase):
    def test_office_inheritence(self):
        # checking is Office is a subclass of Room
        self.assertTrue(issubclass(Office, Room))
#
# # creating aunit test for the create person function
# class TestCasePerson(unittest.TestCase):
#     #
#     # def setUp(self):
#     #     #creating an object andela_dojo_Person from Dojo
#     #     self.andela_dojo_person = Dojo()
#
#     def test_add_person(self, person_name, person_type, wants_accomodation):
#         # creating a person by using person name and person type as parameters from add_person method function
#         #person1 = self.andela_dojo_person.add_person("Neil Armstrong" , "staff")
#         andela_dojo.add_person(person_name, person_type, wants_accomodation)
#
#
#         #person2 = self.andela_dojo_person.add_person("Nelly Armweek" , "Fellow" ,  " Y")
#
#         # checking that self.all_person[0] should be an instance of staff.
#         self.assertTrue(isinstance(self.andela_dojo.all_persons[0], Staff))
#
# #testing to see if Fellow inherits from Person
# class TestCaseFellow(unittest.TestCase):
#     def test_fellow_inheritence(self):
#         #checking is Follow is a subclass of Person
#        self.assertTrue(issubclass(Fellow, Person))
#
# #testing to see if Staff inherits from Person
# class TestCaseStaff(unittest.TestCase):
#     def test_staff_inheritence(self):
#         #checking is Staff is a subclass of Person
#        self.assertTrue(issubclass(Staff, Person))
#

# # The if __name__ == '__main__' convention in python is intended to allow you to write code that
# # can be run directly, or imported. If you import it, that if block is not executed. If you run python.exe myscript.py it is.

if __name__ == "__main__":
    unittest.main()