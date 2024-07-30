#!/usr/bin/python3
"""
This is a command line interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
import shlex
import sys


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB application."""

    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User"]

    def do_quit(self, arg):
        """Exiting the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF."""
        print()
        return True

    def help_quit(self, arg):
        """Help quitting"""
        print("Quit command to exit the program")

    def emptyline(self):
        """Do nothing when empty"""
        pass

    def do_create(self, arg):
        "create <class_name>"
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_ins = eval(f"{commands[0]}()")
            storage.save()
            print(new_ins.id)

    def do_show(self, arg):
        """prints the string representation"""
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            obj = storage.all()

            key = "{}.{}".format(commands[0], commands[1])
            if key in obj:
                print(obj[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance of a class"""
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            obj = storage.all()

            key = "{}.{}".format(commands[0], commands[1])
            if key in obj:
                del obj[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints representation of all instances"""
        obj = storage.all()

        commands = shlex.split(arg)

        if len(commands) == 0:
            for key, value in obj.items():
                print(str(value))
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, value in obj.items():
                if key.split('.')[0] == commands[0]:
                    print(str(value))

    def do_update(self, arg):
        """updates an instance"""
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])

            if key not in objects:
                print("** no instance found **")
            elif len(commands) < 3:
                print("** attribute name missing **")
            elif len(commands) < 4:
                print("** value missing **")
            else:
                obj = objects[key]

                attr_name = commands[2]
                attr_value = commands[3]

                try:
                    attr_value = eval(attr_value)
                except Exception:
                    pass
                setattr(obj, attr_name, attr_value)

                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
