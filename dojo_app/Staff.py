#importing from class Person
from .import Person

#creating class person
class Staff(Person):
    def __init__(self, role, ):
        self.role = role
        self.office = None