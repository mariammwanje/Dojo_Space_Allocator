Introduction

This System/Application requires you to know Programming Basics, Data Structures, Object-Oriented Programming (OOP)
and Test Driven Development (TDD) in Python.

It allocates or assigns office space and optional livivng space to person who are to join Andela,
When a new Fellow joins Andela he/she is assigned an office space and an optional living space if they choose to opt in,
and for a new Staff joins they are assigned an office space only. .



Set Up

        Reccomended python version is python 3.0 and so on;

            * Clone this repo
            * Create a virtual enviroment
            * Activate virtual enviroment
            * Install project requirements
            * run project

System Commands
        Below are the commands to be used;

                *add_person <first_name> <last_name> <role> [<wants_accommodation>]

                        This command Adds a person to the system and allocates the person to a random room.
                        There is a wants_accommodation were by there is an optional argument which can be either Y
                        or N. The default value if it is not provided is N.

                *create_room <room_type> <room_name>

                        This Command Creates rooms in the Dojo, the user should be able to create as many rooms as
                        possible by specifying multiple room names after the create_room command.

                *Reallocate_Person
                        This commands deals with reallocate_persons





constraints:
        An office can accommodate a maximum of 6 people.
        A living space can accommodate a maximum of 4 people.
        A person to be allocated could be a fellow or staff.
        Staff cannot be allocated living spaces.
        Fellows have a choice to choose a living space or not.
        This system will be used to automatically allocate spaces to people at random.



Features: