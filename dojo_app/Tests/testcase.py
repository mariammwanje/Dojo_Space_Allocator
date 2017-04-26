import unittest


from dojo_app.Dojo import Dojo
from dojo_app.Staff import Staff
from dojo_app.LivingSpace import LivingSpace
from dojo_app.Room import Room
from dojo_app.Fellow import Fellow
from dojo_app.Office import Office
from dojo_app.Person import Person




class TestCaseRoom(unittest.TestCase):

    def setUp(self):
        self.andela_dojo_room = Dojo()

#creating aunit test for the create room function
    def test_create_room(self):
        #creating a room by using room name ad room type as parameters from create_room function
        created_room1 = self.andela_dojo_room.create_room("Orange", "office")
        created_room2 = self.andela_dojo_room.create_room("Orange", "living_space")

    # checking that self.all_rooms[0] should be an instance of office.
        self.assertTrue(isinstance(self.andela_dojo_room.all_rooms[0], Office))


# creating aunit test for the create person function
class TestCasePerson(unittest.TestCase):
    #
    def setUp(self):
        #creating an object andela_dojo_Person from Dojo
        self.andela_dojo_person = Dojo()

    def test_add_person(self):
        # creating a person by using person name and person type as parameters from add_person method function
        person1 = self.andela_dojo_person.add_person("Neil Armstrong" , "staff")

        #person2 = self.andela_dojo_person.add_person("Nelly Armweek" , "Fellow" ,  " Y")

        # checking that self.all_person[0] should be an instance of staff.
        self.assertTrue(isinstance(self.andela_dojo_person.all_persons[0], Staff))

#testing to see if Fellow inherits from Person
class TestCaseFellow(unittest.TestCase):
    def test_fellow_inheritence(self):
        #checking is Follow is a subclass of Person
       self.assertTrue(issubclass(Fellow, Person))

#testing to see if Staff inherits from Person
class TestCaseStaff(unittest.TestCase):
    def test_staff_inheritence(self):
        #checking is Staff is a subclass of Person
       self.assertTrue(issubclass(Staff, Person))

# testing to see if LivingSpace inherits from Room
class TestCaseLivingSpace(unittest.TestCase):
    def test_livingspace_inheritence(self):
        # checking is livingspace is a subclass of Room
        self.assertTrue(issubclass(LivingSpace, Room))

# testing to see if Office inherits from Room
class TestCaseOffice(unittest.TestCase):
    def test_office_inheritence(self):
        # checking is Office is a subclass of Room
        self.assertTrue(issubclass(Office, Room))


# The if __name__ == '__main__' convention in python is intended to allow you to write code that
# can be run directly, or imported. If you import it, that if block is not executed. If you run python.exe myscript.py it is.

if __name__ == "__main__":
    unittest.main()