#!/usr/bin/python3
""" defines the basemodel class """
import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """ represent the basemodel of airbanb project """

    def __init__(self, *args, **kwargs):
        """ initializetion of new basemodel

        args:
            *args: unused
            **kwargs: the par to be used
        """
        vtform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for i, x in kwargs.items():
                if i == "created_at" or i == "updated_at":
                    self.__dict__[i] = datetime.strptime(x, vtform)
                else:
                    self.__dict__[i] = x
        else:
            models.storage.new(self)

    def save(self):
        """ update updated_at with current datetime """
        self.updated_at = datetime.today()

        models.storage.save()

    def to_dict(self):
        """ func to return the dic of basemodel """

        newdict = self.__dict__.copy()

        newdict["created_at"] = self.created_at.isoformat()
        newdict["updated_at"] = self.updated_at.isoformat()
        newdict["__class__"] = self.__class__.__name__

        return newdict

    def __str__(self):
        """ func to return print str representation of basemodel """
        clonename = self.__class__.__name__

        return "[{}] ({}) {}".format(clonename, self.id, self.__dict__)
