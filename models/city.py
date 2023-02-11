#!/usr/bin/python3
""" Defining the City class """
from models.base_model import BaseModel


class City(BaseModel):
    """ Represents a city
    Attributes:
        name(str): The name of the City
        state_id(str): The State Id
    """
    name = ""
    state_id = ""
