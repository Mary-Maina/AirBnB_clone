#!/usr/bin/python3
"""
This is a command line interpreter
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB application."""

    prompt = "(hbnb) "

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
