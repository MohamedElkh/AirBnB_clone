#!/usr/bin/python3
""" define the city class """
from models.base_model import BaseModel


class City(BaseModel):
    """ class rep city with attr stat_id and name """

    state_id = ""
    name = ""
