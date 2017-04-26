"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.

Usage:
    Command
"""

import cmd
import sys

from docopt import docopt

from docopt_decorator import docopt_cmd
from dojo_app.Dojo import Dojo

andela_dojo = Dojo()

class RoomInteractive(cmd.Cmd):
    intro = 'Welcome to  Andela Dojo Space Allocator Program'
    prompt = 'Command  '

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_name> <room_type>"""
        room_name = arg['<room_name>']
        room_type = arg['<room_type>']

        andela_dojo.create_room(room_name, room_type)

        print(room_type + 'called' + room_name + 'has been creatd')

    @docopt_cmd
    def do_add_person(self, arg):
        """"Usage:  add_person <person_name> <person_type>"""
        print(arg)


opt = docopt(__doc__, sys.argv[1:])
RoomInteractive().cmdloop()
