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


