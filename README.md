Introduction

This Application requires you to know Programming Basics, Data Structures, Object-Oriented Programming (OOP)
and Test Driven Development (TDD) in Python.

It allocates or assigns office space and optional livivng space to persons who are to join Andela,
When a new Fellow joins Andela he/she is assigned an office space and an optional living space if they choose to opt in,
and for a new Staff, they are assigned an office space only. .



Set Up

        Reccomended python version is python 3.0 and so on;

            * Clone this repository
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

                *print_room <room_name>
                        Prints  the names of all the people in room_name on the screen.

                *print_allocations [-o=filename]
                        Prints a list of allocations onto the screen. Specifying the optional -o option here
                        outputs the registered allocations to a txt file.

                *print_unallocated [-o=filename]
                        Prints a list of unallocated people to the screen. Specifying the -o option here outputs
                        the information to the txt file provided.

                *reallocate_person <person_identifier> <new_room_name>
                        Reallocate the person with person_identifier to new_room_name.

                *load_people
                        Adds people to rooms from a txt file.

                *save_state [--db=sqlite_database]
                        Persists all the data stored in the app to a SQLite database. Specifying the
                        --db parameter explicitly stores the data in the sqlite_database specified.

                *load_state <sqlite_database>
                        Loads data from a database into the application.


constraints:
        An office can accommodate a maximum of 6 people.
        A living space can accommodate a maximum of 4 people.
        A person to be allocated could be a fellow or staff.
        Staff cannot be allocated living spaces.
        Fellows have a choice to choose a living space or not.
        This system will be used to automatically allocate spaces to people at random.


