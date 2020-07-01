#!/usr/bin/python3
"""
FileStorage class file
"""
from models.base_model import BaseModel
import json
import models
class FileStorage:
    ''' File Storage class'''
    __file_path = 'file.json'
    __objects = {}

    def all(self): 
        return self.__objects

    def new(self, obj):
        c = obj.__class__.__name__ + "." + obj.id
        self.__objects[c] = obj

    def save(self):
        d = {}
        for key, value in self.__objects.items():
            d[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(d, f)
            
    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                dic = json.load(f)

            for keys in dic.keys():
                self.__objects[keys] = BaseModel(**dic[keys])
        except FileNotFoundError:
            pass