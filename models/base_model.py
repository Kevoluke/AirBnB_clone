#!/usr/bin/python3
""" Defines The BaseModel class """
from datetime import datetime
import models
from uuid import uuid4


class BaseModel:
    """ Class representing BaseModel of Airbnb-clone Project """

    def __init__(self, *args, **kwargs):
        """Initializes instance attributes
        Args:
        - *args: list of arguments
        - **kwargs: dict of key-values arguments
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        timeform = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            models.storage.new(self)

    def save(self):
        """ Updating updated_at with the current datetime """
        self.updated_at = datetime.today()
        models.storage.new(self)
        models.storage.save()

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
