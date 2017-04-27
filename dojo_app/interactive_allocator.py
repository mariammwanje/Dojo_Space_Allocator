"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.

Usage:
    Command
"""

import cmd
import sys

from docopt import docopt

from dojo_app.Dojo import Dojo
from dojo_app.docopt_decorator import docopt_cmd

andela_dojo = Dojo()

class RoomInteractive(cmd.Cmd):
    intro = 'Welcome to  Andela Dojo Space Allocator Program'
    prompt = 'Command  '

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room  <room_type> <room_name>... """
        # equating arg room_type to its arg
        room_type = arg['<room_type>']
        #equating arg room_name to its arg
        room_name = arg['<room_name>']

        # loop for printing multiple rooms at once
        for room in room_name:

        #creating room from object andela_dojo
            andela_dojo.create_room( room_type, room_name)
        #print message
            print(room_type  + room_name  +  'has been successfully created!')

    @docopt_cmd
    def do_add_person(self, arg):
        """"Usage: add_person  <person_type> <person_name> [<wants_accomodation>]

        """
        # equating arg person_type
        person_type = arg['<person_type>']
        #equating arg person_name
        person_name = arg['<person_name>']
        #equating arg wants_accomodation
        wants_accomodation = arg['<wants_accomodation>']
        andela_dojo.add_person(person_name, person_name, wants_accomodation)
        #creating person from object andela_dolo
        print(andela_dojo.add_person(person_type, person_name, wants_accomodation))
        #print message

    @docopt_cmd
    def do_print_rooms(self, arg):
        """Usage:print_rooms <room_name>
        """
        #equating a list of room names
        room_name = arg
        #printing a list of room names
        andela_dojo.print_rooms(room_name)
        print(andela_dojo.print_rooms(room_name))


opt = docopt(__doc__, sys.argv[1:])
RoomInteractive().cmdloop()
