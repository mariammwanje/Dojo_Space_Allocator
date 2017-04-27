import unittest

from dojo_app.Dojo import Dojo
from dojo_app.Fellow import Fellow
from dojo_app.LivingSpace import LivingSpace
from dojo_app.Office import Office
from dojo_app.Person import Person
from dojo_app.Room import Room
from dojo_app.Staff import Staff


class TestCaseRoom(unittest.TestCase):
    #creating aunit test for the create room function
    def test_create_room(self):
        #creating an object andela_dojo from Dojo class
        andela_dojo = Dojo()
        initial_room_count = len(andela_dojo.all_rooms)
        #creating an object andela_dojo from Dojo class
        blue_office = andela_dojo.create_room('Blue', 'office')
        self.assertTrue(blue_office)
        new_room_count = len(andela_dojo.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)
        # checking that self.all_rooms[0] should be an instance of office.
        # self.assertTrue(isinstance(self.andela_dojo.all_rooms[0], Office))


class TestCasePerson(unittest.TestCase):
    def test_add_person(self):
        #creating an object andela_dojo_Person from Dojo
        andela_dojo = Dojo()
    #initial number of persons
        initial_person_count = len(andela_dojo.all_persons)
        # creating a person by using person name and person type as parameters from add_person method function
        person1 = andela_dojo.add_person("Neil Armstrong" , "staff", "Y")
        self.assertTrue(person1)
        new_person_count = len(andela_dojo.all_persons)
        self.assertEqual(new_person_count - initial_person_count, 1)
            # creating a person by using person name and person type as parameters from add_person method function
            #person1 = self.andela_dojo_person.add_person("Neil Armstrong" , "staff")
            #andela_dojo.add_person(person_name, person_type, wants_accomodation)




# # # testing to see if LivingSpace inherits from Room
class TestCaseLivingSpace(unittest.TestCase):
    def test_livingspace_inheritence(self):

        # checking is livingspace is a subclass of Room
        self.assertTrue(issubclass(LivingSpace, Room))

# # testing to see if Office inherits from Room
class TestCaseOffice(unittest.TestCase):
    def test_office_inheritence(self):
        # checking is Office is a subclass of Room
        self.assertTrue(issubclass(Office, Room))
#

# #testing to see if Fellow inherits from Person
class TestCaseFellow(unittest.TestCase):
    def test_fellow_inheritence(self):
        #checking is Follow is a subclass of Person
       self.assertTrue(issubclass(Fellow, Person))
#
# #testing to see if Staff inherits from Person
class TestCaseStaff(unittest.TestCase):
    def test_staff_inheritence(self):
        #checking is Staff is a subclass of Person
       self.assertTrue(issubclass(Staff, Person))
#

# # The if __name__ == '__main__' convention in python is intended to allow you to write code that
# # can be run directly, or imported. If you import it, that if block is not executed. If you run python.exe myscript.py it is.

if __name__ == "__main__":
    unittest.main()