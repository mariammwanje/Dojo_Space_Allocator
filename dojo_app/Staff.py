#importing from class Person

#creating class person
from .Person import Person


class Staff(Person):
    # initializing the attributes of class staff
    def __init__(self, person_name):
        # inheriting to from class Person the person_name and type staff
        Person.__init__(Person, person_name, 'staff')