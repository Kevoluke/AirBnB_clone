#!/usr/bin/python3
""" Defining the Review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Represents a user's Review
    Attributes:
        place_id(str): The Place id
        user_id(str): The User's id
        text(str): The text of the Review
    """
    place_id = ""
    user_id = ""
    text = ""
