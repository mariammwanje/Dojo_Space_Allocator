# importing from class Person
from . import Person


# creating fellow class
class Fellow(Person):
#list that contains all my fellows that exits
    my_fellows = []
#method that loads fellows that exist in the database
    def load_fellows(self, fellows):

        if type(fellows) is list:
            Fellow.fellow_names.extend(fellows)
            return 'Fellow names loaded successfully'
        else:
            return ' Failed: Incorrect Fellow details'

    def add_one_fellow(self, name):
        if type(name) is str:
            Fellow.my_fellows.append(name)
            return True
        else:
            return '\t\t Failed: Incorrect Fellow details'
