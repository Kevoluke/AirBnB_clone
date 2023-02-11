#!/usr/bin/python3
""" Defining the State class """
from models.base_model import BaseModel


class State(BaseModel):
    """ Represents a state
    Attributes:
        name(str): The Nmae of the State
    """
    name = ""
