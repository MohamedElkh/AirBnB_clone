#!/usr/bin/python3
""" define the console """
import re
import cmd
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User


def parse(arg):
    cl_braces = re.search(r"\{(.*?)\}", arg)
    brackt = re.search(r"\[(.*?)\]", arg)

    if cl_braces is None:
        if brackt is None:
            return [x.strip(",") for x in split(arg)]
        else:
            lx = split(arg[:brackt.span()[0]])
            rt = [x.strip(",") for x in lx]
            rt.append(brackt.group())
            return rt
    else:
        lx = split(arg[:cl_braces.span()[0]])
        rt = [x.strip(",") for x in lx]
        rt.append(cl_braces.group())
        return rt


class HBNBCommand(cmd.Cmd):
    """ define the class HBNBCommand
    attr:
        prom: the command prompt
    """

    prom = "(hbnb) "

    __classes = {"BaseModel", "User", "State", "City",
                 "Place", "Amenity", "Review"}

    def emptylinee(self):
        """ func to do nothing """
        pass

    def default(self, arg):
        """ func to default the behavior for cmd """
        rdict = {
                "all": self.do_all, "show": self.do_show,
                "destroy": self.do_destroy, "count": self.do_count,
                "update": self.do_update
                }

        mtch = re.search(r"\.", arg)

        if mtch is not None:
            g1 = [arg[:mtch.span()[0]], arg[mtch.span()[1]:]]

            mtch = re.search(r"\((.*?)\)", arg[1])

            if mtch is not None:
                com = [argl[1][:mtch.span()[0]], mtch.group()[1:-1]]
                if com[0] in rdict.keys():
                    cl = "{} {}".format(argl[0], com[1])
                    return rdict[com[0]](cl)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def quit(self, arg):
        """ func to quit the command to exit """
        return True

    def EOF(self, arg):
        """ func eof signal to exit """
        print("")
        return True

    def create(self, arg):
        """ func to create new class """
        g1 = parse(arg)

        if len(g1) == 0:
            print("** class name missing **")
        elif g1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(g1[0])().id)
            storage.save()

    def show(self, arg):
        """ func to display the str rep of class """
        g1 = parse(arg)
        obdict = storage.all()

        if len(g1) == 0:
            print("** class name missing **")
        elif g1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(g1) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(g1[0], g1[1]) not in obdict:
            print("** no instance found **")
        else:
            print(obdict["{}.{}".format(g1[0], g1[1])])

    def destroy(self, arg):
        """ func to destroy class """
        g1 = parse(arg)
        obdict = storage.all()

        if len(g1) == 0:
            print("** class name missing **")
        elif g1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(g1) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(g1[0], g1[1]) not in obdict.keys():
            print("** no instance found **")
        else:
            del obdict["{}.{}".format(g1[0], g1[1])]
            storage.save()

    def all(self, arg):
        """ func to display all strings """
        g1 = parse(arg)

        if len(g1) > 0 and g1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            ob = []

            for obj in storage.all().values():
                if len(g1) > 0 and g1[0] == obj.__class__.__name__:
                    ob.append(obj.__str__())
                elif len(g1) == 0:
                    ob.append(obj.__str__())
            print(ob)

    def do_count(self, arg):
        """ func to count and retrive the num """
        g1 = parse(arg)
        num = 0

        for obj in storage.all().values():
            if g1[0] == obj.__class__.__name__:
                num += 1
        print(num)

    def update(self, arg):
        """ func to update key and value """
        g1 = parse(arg)
        obdict = storage.all()

        if len(g1) == 0:
            print("** class name missing **")
            return False
        if g1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(g1) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(g1[0], g1[1]) not in obdict.keys():
            print("** no instance found **")
            return False
        if len(g1) == 2:
            print("** attribute name missing **")
            return False
        if len(g1) == 3:
            try:
                type(eval(g1[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(g1) == 4:
            obj = obdict["{}.{}".format(g1[0], g1[1])]
            if g1[2] in obj.__class__.__dict__.keys():
                vtype = type(obj.__class__.__dict__[g1[2]])
                obj.__dict__[g1[2]] = vtype(g1[3])
            else:
                obj.__dict__[g1[2]] = g1[3]
        elif type(eval(g1[2])) == dict:
            obj = obdict["{}.{}".format(g1[0], g1[1])]

            for x, a in eval(g1[2]).items():
                if (x in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[x]) in {str, int, float}):
                    vtype = type(obj.__class__.__dict__[x])
                    obj.__dict__[x] = vtype(a)
                else:
                    obj.__dict__[x] = a

        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
