# importing from class Person


# creating fellow class
from dojo_app.Person import Person


class Fellow(Person):
    def __init__(self, person_name, wants_accomodation ):
        pass
        #inheriting to from class Person the person_name and type fellow
        super(Fellow, self).__init__(person_name, "fellow", wants_accomodation )