#!/usr/bin/python3
""" Defining The Place class """
from models.base_model import BaseModel


class Place(BaseModel):
    """ Represents a Place
    Attributes:
        city_id(str): The City id.
        user_id(str): The User id
        name(str): The name of the Place
        description(str): The description of the Place
        number_rooms(int): The number of rooms in the Place
        number_bathrooms(int): The number of bathrooms int the Place
        max_guest(int): The maximum number of guests allowed in the Place
        price_by_night(int): The price per night of the Place
        latitude(float): The latitudinal coordinates of the Place
        longitude(float): The longitudinal coordinates of the Place
        amenity_ids(list): A list of Amenity ids of the Place
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
