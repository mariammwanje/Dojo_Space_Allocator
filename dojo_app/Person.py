class Person(object):
#addition of a coomodation parameter
    def __init__(self, person_name, person_type, wants_accomodation):
        self.person_name = person_name
        self.person_type = person_type
        self.wants_accomodation = wants_accomodation


person1 = Person('Mariam', 'girl', 'yes')
print(person1.person_type)
print(person1.person_name)
print(person1.wants_accomodation)
print(person1)
