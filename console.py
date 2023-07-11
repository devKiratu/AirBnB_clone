#!/usr/bin/python3
"""contains the entry point of the command interpreter"""


import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the functionality of the command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        exit()

    def do_EOF(self, line):
        """Exits the command interpreter on the 'EOF' command\n"""
        return True

    def postloop(self):
        """Adds an empty line before the interpreter exits\n"""
        print()

    def emptyline(self):
        """Blocks execution for empty line + Enter"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
