#!/usr/bin/python3
"""
BaseModel class file
"""
from datetime import datetime
import uuid
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.updated_at = datetime.now()
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        '''str repr'''
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''save method'''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''returns __dict__ representation of an instance'''
        d = self.__dict__.copy()
        d['updated_at'] = d['updated_at'].isoformat()
        d['created_at'] = d['created_at'].isoformat()
        d['__class__'] = self.__class__.__name__
        return d
