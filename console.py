#!/usr/bin/python3
"""
This is a command line interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models
import shlex
import sys


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB application."""

    prompt = "(hbnb) "
    valid_classes = [
            "BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

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

    def default(self, arg):
        """Default behavior for cmd syntax"""
        arg_list = arg.split('.')
        if len(arg_list) != 2:
            print("*** Unknown syntax: {}".format(arg))
            return False

        inc_cls = arg_list[0]
        command = arg_list[1].split('(')
        if len(command) != 2:
            print("*** Unknown syntax: {}".format(arg))
            return False

        inc_method = command[0]
        extra_arg = command[1].split(')')[0]
        all_args = extra_arg.split(',')

        m_dict = {
                'all': self.do_all,
                'show': self.do_show,
                'update': self.do_update,
                'destroy': self.do_destroy,
                'count': self.do_count,
                }

        if inc_method in m_dict.keys():
            if inc_method != "update":
                return m_dict[inc_method]("{} {}".format(inc_cls, extra_arg))
            else:
                obj_id = all_args[0]
                attr_name = all_args[1]
                attr_value = all_args[2]

                return m_dict[inc_method]("{} {} {} {}".format(
                    inc_cls, obj_id, attr_name, attr_value))

        print("*** Unknown Syntax: {}".format(arg))
        return False

    def do_count(self, arg):
        """counts the number of instances"""
        objects = storage.all()

        commands = shlex.split(arg)

        if arg:
            inc_cls = commands[0]

        count = 0

        if commands:
            if inc_cls in self.valid_classes:
                for obj in objects.values():
                    if obj.__class__.__name__ == inc_cls:
                        count += 1
                print(count)
            else:
                print("** class doesn't exist **")
        else:
            print("** class doesn't exist **")

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
