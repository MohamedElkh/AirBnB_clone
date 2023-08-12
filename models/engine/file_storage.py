#!/usr/bin/python3
""" define the file storage """
import json
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel
from models.user import User
from models.state import State


class FileStorage:
    """ func to represent the storage engine

    attributes:
        __file_path: the name of the file
        __objects: the dic of objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ func to return the dict __object """
        return FileStorage.__objects

    def new(self, obj):
        """ func to set objects with key id """
        cname = obj.__class__.__name__

        FileStorage.__objects["{}.{}".format(cname, obj.id)] = obj

    def save(self):
        """ func to serialize the objects to json """
        oodict = FileStorage.__objects
        obdict = {obj: oodict[obj].to_dict() for obj in oodict.keys()}

        with open(FileStorage.__file_path, "w") as f:
            json.dump(obdict, f)

    def reload(self):
        """ func to turn the json file to object """
        try:
            with open(FileStorage.__file_path) as f:
                obdict = json.load(f)

                for o in obdict.values():
                    cl_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cl_name)(**o))

        except FileNotFoundError:
            return
