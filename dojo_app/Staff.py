#importing from class Person

#creating class person
from dojo_app import Person


class Staff(Person):
    # initializing the attributes of class staff
    #addition of accomodation as a parameter
    def __init__(self, person_name , wants_accomodation):
        # inheriting to from class Person the person_name and type staff
        Person.__init__(Person, person_name, 'staff', wants_accomodation)