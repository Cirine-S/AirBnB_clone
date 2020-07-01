#!/usr/bin/python3
'''review module'''
from models.base_model import BaseModel
import models


class Review(BaseModel):
    '''review class'''
    place_id = ''
    user_id = ''
    text = ''