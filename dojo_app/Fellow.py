# importing from class Person


# creating fellow class
from dojo_app.Person import Person


class Fellow(Person):
    # initializing the attributes of class fellow
    #addition of accomodation as a parameter

    def __init__(self, person_name, wants_accomodation):
        #inheriting to from class Person the person_name and type fellow
        Person.__init__(Person, person_name, 'fellow', wants_accomodation)
