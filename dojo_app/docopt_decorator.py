#addition of the usage command to display what exits in the function
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.

Usage:
    Command
"""
#importing cmd
import cmd
#importing sys
import sys
#importing docopt from docopt class
from docopt import docopt
#importing docopt cmd commands
from docopt_decorator import docopt_cmd
#creating andela_dojo object from Dojo class
from dojo_app.Dojo import Dojo

andela_dojo = Dojo()


class RoomInteractive(cmd.Cmd):
    intro = 'Welcome to  Andela Dojo Space Allocator Program'
    prompt = 'Command  '


    @docopt_cmd
    def do_create_room(self, arg):
        pass

    @docopt_cmd
    def do_add_person(self, arg):
        pass



#printing the file to be pass, sys.argv[1:] recieves inputs as a list from 0 to infinity
opt = docopt(__doc__, sys.argv[1:])
#launching our Cmd L Interface class,its a cmdloop() because it loops everytime and repeats automatically
RoomInteractive().cmdloop()