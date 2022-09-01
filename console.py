#!/usr/bin/python3
"""Python program for AirBnb console
    """

import cmd

from models import storage


import re
import json


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

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
            saves it (to the JSON file)"""
        if arg == "" or arg is None:
            print("** class name missing **")
        elif arg not in storage.classes:
            print("** class doesn't exist **")
        else:
            item = storage.classes()[arg]()
            item.save()
            print(item.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
            based on the class name and id"""
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            word = arg.split(" ")
            if word[0] not in storage.classes:
                print("** class doesn't exist **")
            elif len(word) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(word[0], word[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and
            id (save the change into the JSON file)."""
        pass

    def all(self, arg):
        """Prints all string representation of all
            instances based or not on the class name"""
        pass

    def update(self, arg):
        """Updates an instance based on the class name and id
            by adding or updating attribute (save the change
            into the JSON file)"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
