#!/usr/bin/python3
""" define the class user """
from models.base_model import BaseModel


class User(BaseModel):
    """ rep class user with attrs """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
