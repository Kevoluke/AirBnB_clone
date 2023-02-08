#!/usr/bin/python3
""" Defines The BaseModel class """
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ Class representing BaseModel of Airbnb-clone Project """

    def __init__(self):
        """ function initializing a new BaseModel """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        timeform = "%Y-%m-%dT%H:%M:%S.%f"

    def save(self):
        """ Updating updated_at with the current datetime """
        self.updated_at = datetime.today()

    def to_dict(self):
        """ Returns the dictionary of BaseModel instance """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """ Returns/prints the string representation of BaseModel instance """

        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
