# importing from class Person


# creating fellow class
from .Person import Person


class Fellow(Person):
    # initializing the attributes of class fellow
    def __init__(self, person_name):
        #inheriting to from class Person the person_name and type fellow
        Person.__init__(Person, person_name, 'fellow')
