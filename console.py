#!/usr/bin/python3
"""Python program for AirBnb console
	"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the HBnB command interpreter.
    
    """
    
    prompt = "(hbnb) "
    
    
    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass
    
    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True
    

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True
    