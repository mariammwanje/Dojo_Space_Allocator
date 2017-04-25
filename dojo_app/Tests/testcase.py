import unittest
#importing LivingSpace from Class Room
from dojo_app.LivingSpace import LivingSpace
#testing to check if LivingSpace inherits from aclass Room
from dojo_app.Office import Office
# from .Dojo_Space_Allocator.dojo_app import Fellow
from dojo_app.Fellow import Fellow
# importing Staff from Class Staff
from dojo_app.Staff import Staff

#testing to check if LivingSpace inherits from class Room
class LivingSpaceTestCase(unittest.TestCase):

    #function for checking whether LivingSpace inherits from Room
    def does_livingspace_inherit(self):
        #assertTrue means checking if the value is true ie assertTrue(a): check the value of a is True
        #assert: base assert allowing you to write your own assertions
        self.assertTrue(issubclass(LivingSpace, object))




#testing to check if Office inherits from aclass Room
class OfficeTestCase(unittest.TestCase):

    #function for checking whether Office inherits from Room
    def does_office_inherit(self):
        self.assertTrue(issubclass(Office, object))




#testing to check if a felow inherits from aclass person
class FellowTestCase(unittest.TestCase):

    #function for checking whether fellow inherits from Person
    def does_fellow_inherit(self):
        self.assertTrue(issubclass(Fellow, object))

    def is_allocated_space(self):
        self.assertEquals()



#testing to check if a Staff inherits from aclass Person
class TestCase(unittest.TestCase):

    #function for checking whether Staff inherits from Person
    def does_staff_inherit(self):
        self.assertTrue(issubclass(Staff, object))