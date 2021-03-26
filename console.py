#!/usr/bin/python3
"""Console File to handle objects"""
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """The console of the Airbnb project"""
    prompt = "(hbnb) "
    class_list = ["BaseModel", "User", "City", "State", "Amenity",
                  "Place", "Review"]
    # Non changeable atributes:
    attr_list = ["updated_at", "created_at", "id"]

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Do nothing with an empty line"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file)"""
        if len(line) == 0 or line == "":
            print("** class name missing **")
        elif line in HBNBCommand.class_list:
            """klass = globals()[line]
            new_inst = klass()
            new_inst.save()"""
            # to evaluate an expression dinamically, converts the line into a class
            print(eval(line)().id)
            # to serialize:
            storage.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id"""
        # all returns __objects dict
        objs = storage.all()
        if not line or len(line) == 0:
            print('** class name missing **')
        else:
            arg = line.split()
            # args starts in class name [0]
            if not arg[0] in HBNBCommand.class_list:
                print("** class doesn't exist **")
            elif len(arg) == 1:
                print('** instance id missing **')
            elif (arg[0] + "." + arg[1]) not in objs:
                print('** no instance found **')
            else:
                    print(objs[arg[0] + "." + arg[1]])

    def do_all(self, line):
        '''
        Prints all string representation of all instances
        based or not on the class name
        '''
        new_list = []
        arg = line.split()
        objs = storage.all()
        if len(arg) == 0:
            for val in objs.values():
                new_list.append(val.__str__())
            print(new_list)
        elif arg[0] in HBNBCommand.class_list:
            for class_key in objs:
                if arg[0] in class_key:
                    new_list.append(objs[class_key].__str__())
            print(new_list)
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes an instance
        based on the class name and id"""
        objs = storage.all()
        if line != "" or len(line) != 0:
            args = line.split()
            if args[0] not in HBNBCommand.class_list:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            elif len(args) == 2:
                key = args[0] + "." + args[1]
                if key in objs:
                    del objs[key]
                    storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_update(self, line):
        """updates an instance based on the class name and id"""
        objs = storage.all()
        scape = ["\"", "\'"]
        if line != "" or len(line) != 0:
            args = line.split()
            if args[0] not in HBNBCommand.class_list:
                print("** class doesn't exist **")
                return False
            if len(args) == 1:
                print("** instance id missing **")
                return False
            if "{}.{}".format(args[0], args[1]) not in objs.keys():
                print("** no instance found **")
                return False
            if len(args) == 2:
                print("** attribute name missing **")
            if len(args) == 3:
                print("** value missing **")
                return False
            if len(args) >= 4:
                key = args[0] + "." + args[1]
                if key in objs:
                    if args[2] not in HBNBCommand.attr_list:
                        # arg[3][-1] is the last character of the string
                        if args[3][0] in scape and args[3][-1] in scape:
                            # arg [3] goes from 1 to menus 1, without ""
                            setattr(objs[key], args[2], str(args[3][1:-1]))
                        else:
                            setattr(objs[key], args[2], str(args[3]))
                            # saves in file
                        storage.save()
                else:
                    print("** no instance found **")
                    return False
        else:
            print("** class name missing **")

    def count(self, line):
        """Return the amount of instances of the class"""
        count = 0
        objs = storage.all()
        if line in HBNBCommand.class_list:
            for class_key in objs:
                if line in class_key:
                    count += 1
            print(count)

    def default(self, line):
        """In case to not found any command this func is executed"""
        functions = {"all": HBNBCommand.do_all, "count": HBNBCommand.count}
        functions_parameters = {"show": HBNBCommand.do_show,
                                "destroy": HBNBCommand.do_destroy}
        try:
            args = line.split(".")
            name_func = ""
            func_id = ""
            # enumerate returns letter by letter and puts and index
            for index, letter in enumerate(args[1]):
                if letter == "(":
                    # ex: user.show takes only show
                    name_func = args[1][0:index]
                    break
            # now I have name function
            if name_func in functions:
                # calls do_all or do_count and pass args [0] which is the class
                functions[name_func](self, args[0])
            elif name_func in functions_parameters:
                # args[0] is class, args[1] is id +2 to saltear paréntesis and comillas,
                # same for -2
                line = args[0] + " " + args[1][index + 2:-2]
                # line is gonna be: user id
                functions_parameters[name_func](self, line)
            elif name_func == "update":
                parse = ""
                line = args[1][index + 1:-1]
                for letter in line:
                    if letter != '"' and letter != "'":
                    # ya no tiene comillas
                        parse += letter
                parse = parse.split(",")
                line = args[0] + " "
                for elem in parse:
                    elem.strip(" ")
                    line += elem + " "
                HBNBCommand.do_update(self, line)
            else:
                print("*** Unknown syntax: {}".format(line))
        except:
            print("*** Unknown syntax: {}".format(line))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
