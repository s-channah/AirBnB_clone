#!/usr/bin/env python3
"""
This is the console interaction with the user
We all began somewhere
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity
from models import FileStorage
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """
    This is a class for the command interpreter
    """

    prompt = "(hbnb) "
    class_identifier = ("BaseModel", "User", "Amenity",
                        "Place", "City", "State", "Review")

    def precmd(self, line):
        """
        This is the access to the console
        line: this is the input command/argurement
        """
        if not line:
            pass
        else:
            if line.split()[0] in ("create", "count", "all", "show",
                                   "update", "destroy"):
                return line
            else:
                class_name = line.split(".")[0]
                try:
                    inpcmd = line.split(".")[1].strip(")")
                    cmd_inp = inpcmd.strip("(")
                    return " ".join([cmd_inp, class_name])
                except IndexError:
                    pass
                return class_name
        return line

    def do_EOF(self, arg):
        """
        EOF command to Exit program
        """
        return True

    def do_create(self, arg):
        """
        This creates new instances
        """
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg.strip() in HBNBCommand.class_identifier:
            obj = eval(arg.strip())()
            storage.save()
            print(obj.id)
        else:
            print("** class name does not exist **")

    def do_quit(self, arg):
        """
        Quit command to exit program
        """
        return True

    def emptyline(self):
        """
        method empty
        """
        pass

    def do_count(self, arg):
        """
        This counts the number of instances of a particular
        class
        """
        count = 0
        for item in storage.all().keys():
            if arg == item.split(".")[0]:
                count += 1
        print(count)

    def do_all(self, arg):
        """
        This is a method that displqys all available objects
        param : all - shows all
        param : all User - shows all users
        """
        obj_list = []
        args = arg.split()
        if len(args) >= 1:
            if args[0] in HBNBCommand.class_identifier:
                key = args[0]
                for item, value in storage.all().items():
                    if item.startswith(key):
                        obj_list.append(str(value))
                print(obj_list)
            else:
                print("** Class doesn't exist **")
        elif len(args) == 0:
            for values in storage.all().values():
                obj_list.append(str(values))
            print(obj_list)

    def do_show(self, arg):
        """
        This is the method that shows the particular object and its id
        eg show User 4545212
        """
        args = arg.split()
        if len(args) >= 2:
            if args[0] not in HBNBCommand.class_identifier:
                print("** class doesn't exist **")
            else:
                key = args[0] + args[1]
                if key in storage.all():
                    print(storage.all().get(key))
                else:
                    print("** no instance found **")
        elif len(args) == 1:
            if args[0] not in HBNBCommand.class_identifier:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(args) == 0:
            print("** class name missing **")

    def do_update(self, arg):
        """
        This updates ther attributes of an object by passing the
        ID; ATTRIBUTES. VALUES
        eg. BaseModel 54512212 user.last_name JENKO
        """
        args = arg.split()
        if len(args) >= 4:
            if args[0] in HBNBCommand.class_identifier:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    setattr(storage.all()[key], args[2],
                            str(arg[3].strip('"')))
                    storage.save()
                else:
                    print("** No instance Found **")
            else:
                print("** Class doesn't exist **")
        elif len(args) == 3:
            if args[0] in HBNBCommand.class_identifier:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    print("** Value missing **")
                else:
                    print("** no instance found **")
            else:
                print("** Class doesn't exist **")
        elif len(args) == 2:
            if args[0] in HBNBCommand.class_identifier:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    print("** Attribute name missing **")
                else:
                    print("** No instances found **")
            else:
                print("** Class doesn't Exist **")
        elif len(args) == 1:
            if args[0] in HBNBCommand.class_identifier:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** Class name Missing **")

    def do_destroy(self, arg):
        """
        This mlethod works to deleting an object by passing
        objects class and id
        ex
        destroy User 555d4sdf4g65df46g
        """
        args = arg.split()
        if len(args) >= 2:
            if args[0] in HBNBCommand.class_identifier:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    storage.destroy(key)
                else:
                    print("** no instance found **")
            else:
                print("** Class doesn't exist **")
        elif len(args) == 1:
            if args[0] in HBNBCommand.class_identifier:
                print("** instance id missing **")
            else:
                print("** Class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
