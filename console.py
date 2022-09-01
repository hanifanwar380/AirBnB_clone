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

    def default(self, arg):
        """Catch commands if nothing else matches then."""
        # print("DEF:::", line)
        self._precmd(arg)

    def _precmd(self, arg):
        """Intercepts commands for class.syntax()"""

        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", arg)
        if not match:
            return arg
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(
                    1) or "") + " " + (match_attr_and_value.group(2) or "")
        command = method + " " + classname + " " + uid + " " + attr_and_value
        self.onecmd(command)
        return command

    def update_dict(self, classname, uid, s_dict):
        """Helper method for update() with a dictionary."""
        strr = s_dict.replace("'", '"')
        dump = json.loads(strr)
        if not classname:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[classname]
                for attribute, value in dump.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

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

    def do_count(self, line):
        """Counting the instance of a class.
        """
        words = line.split(' ')
        if not words[0]:
            print("** class name missing **")
        elif words[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            matches = [
                keyword for keyword in storage.all() if keyword.startswith(
                    words[0] + '.')]
            print(len(matches))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
