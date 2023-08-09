#!/usr/bin/python3
""" define the class review """
from models.base_model import BaseModel


class Review(BaseModel):
    """ class rep a review """

    place_id = ""
    user_id = ""
    text = ""
