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
        elif arg not in storage.classes():
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
            if word[0] not in storage.classes():
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

        if arg == "" or arg is None:
            print("** class name missing **")

        else:
            words = arg.split(" ")
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, arg):
        """Prints all string representation of all
            instances based or not on the class name"""

        if arg != "":
            words = arg.split(' ')

            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                line = [str(obj) for key, obj in storage.all().items()
                        if type(obj).__name__ == words[0]]
                print(line)
        else:
            line = [str(obj) for key, obj in storage.all().items()]
            print(line)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
            by adding or updating attribute (save the change
            into the JSON file)"""

        if arg == "" or arg is None:
            print("** class name missing **")
            return

        regx = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'

        match = re.search(regx, arg)

        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)

        if not match:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")

        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")

            else:
                type_cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        type_cast = float
                    else:
                        type_cast = int

                else:
                    value = value.replace('"', '')

                attributes = storage.attributes()[classname]

                if attribute in attributes:
                    value = attributes[attribute](value)

                elif type_cast:
                    try:
                        value = type_cast(value)
                    except ValueError:
                        pass  # fine, stay a string then
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
