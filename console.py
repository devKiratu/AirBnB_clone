#!/usr/bin/python3
"""contains the entry point of the command interpreter"""


import cmd
import json
import shlex
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Defines the functionality of the command interpreter"""
    prompt = "(hbnb) "
    __allowed_classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
            }

    def do_create(self, class_name):
        """Creates a new instance of BaseModel or its children, saves it
            (to the JSON file) and prints the id.
        """
        if not class_name:
            print("** class name missing **")
        elif class_name not in self.__allowed_classes.keys():
            print("** class doesn't exist ** ")
        else:
            obj = self.__allowed_classes[class_name]()
            obj.save()
            print(obj.id)

    def do_show(self, args):
        """ Prints the string representation of an instance based on the
        class name and id
        """
        arg_list = args.split()
        if len(arg_list) == 0:
            print("** class name missing **")
            return
        if arg_list[0] not in self.__allowed_classes.keys():
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print("** instance id missing **")
            return
        cls_name, obj_id, *_ = arg_list
        key = "{}.{}".format(cls_name, obj_id)
        all_objs = storage.all()
        if key not in all_objs.keys():
            print("** no instance found **")
        else:
            obj_dict = all_objs[key]
            obj = self.__allowed_classes[cls_name](**obj_dict)
            print(obj)

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id and saves the
        change into the JSON file.
        """
        arg_list = args.split()
        if len(arg_list) == 0:
            print("** class name missing **")
            return
        if arg_list[0] not in self.__allowed_classes.keys():
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print("** instance id missing **")
            return
        cls_name, obj_id, *_ = arg_list
        key = "{}.{}".format(cls_name, obj_id)
        all_objs = storage.all()
        if key not in all_objs.keys():
            print("** no instance found **")
        else:
            del all_objs[key]
            with open("file.json", "w") as f:
                json.dump(all_objs, f)
            storage.reload()

    def do_all(self, args):
        """Prints all string representation of all instances or instances
        based on the class name.
        """
        arg_list = args.split()
        if len(arg_list) == 0:
            all_objs = storage.all()
        else:
            c_name = arg_list[0]
            if c_name not in self.__allowed_classes.keys():
                print("** class doesn't exist **")
                return
            else:
                all_objs = {
                    k: v for k, v in storage.all().items()
                    if v["__class__"] == c_name
                }
        obj_strs = []
        for key in all_objs.keys():
            obj_dict = all_objs[key]
            cls_name = obj_dict["__class__"]
            obj_instance = self.__allowed_classes[cls_name](**obj_dict)
            obj_strs.append(obj_instance.__str__())
        print(obj_strs)

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or
        updating attributes and saving the changes into the JSON file
        """
        arg_list = shlex.split(args)
        all_objs = storage.all()
        if len(arg_list) == 0:
            print("** class name missing ** ")
            return
        if arg_list[0] not in self.__allowed_classes.keys():
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(arg_list[0], arg_list[1])
        if key not in all_objs.keys():
            print("** no instance found **")
            return
        if len(arg_list) == 2:
            print("** attribute name missing **")
            return
        if len(arg_list) == 3:
            print("** value missing **")
            return
        if len(arg_list) >= 4:
            cls_name, obj_id, attr_name, value, *_ = arg_list
            obj_dict = all_objs[key]
            updated_obj = self.__allowed_classes[cls_name](**obj_dict)
            setattr(updated_obj, attr_name, value)
            updated_obj.save()
            storage.new(updated_obj)
            storage.save()

    def default(self, args):
        """Override default behaviour to allow for complex commands"""
        try:
            arg_list = args.split(".")
            if len(arg_list) < 2:
                print("*** Unknown syntax: {}".format(args))
                return
            cls_name, command, *_ = arg_list
            if cls_name not in self.__allowed_classes.keys():
                print("*** Unknown syntax: {}".format(args))
                return
            if command[:-2] == "all" and command.endswith("()"):
                self.do_all(cls_name)
            elif command[:-2] == "count" and command.endswith("()"):
                self.count(cls_name)
            elif command[:4] == "show" and command[4] == "("\
                    and command[-1] == ")":
                obj_id = command[6:-2]
                self.do_show("{} {}".format(cls_name, obj_id))
            else:
                print("*** Unknown syntax: {}".format(args))
        except Exception:
            print("*** Unknown syntax: {}".format(args))

    def do_quit(self, line):
        """Quit command to exit the program
        """
        exit()

    def do_EOF(self, line):
        """Exits the command interpreter on the 'EOF' command
        """
        return True

    def postloop(self):
        """Adds an empty line before the interpreter exits
        """
        print()

    def emptyline(self):
        """Blocks execution for empty line + Enter
        """
        pass

    def count(self, cls_name):
        """prints the number of instances of class represented by 'cls_name'
            Args:
                cls_name: name of class whose number of instances are required
        """
        instance_count = 0
        all_objs = storage.all()
        for key, value in all_objs.items():
            if value["__class__"] == cls_name:
                instance_count += 1
        print(instance_count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
