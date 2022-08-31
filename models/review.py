#!/usr/bin/python3
""" Project HBNB review module """

from models.base_model import BaseModel

class Review(BaseModel):
    """ Review class for storing review information """
    place_id= ""
    user_id= ""
    text= ""
    