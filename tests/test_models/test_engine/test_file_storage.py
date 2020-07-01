#!/usr/bin/python3
''' file storage test '''
import unittest
import time
import pep8
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    ''' Tests FileStorage class '''

    def test0(self):
        ''' test 0 '''
        self.assertEqual(type(storage).__name__, 'FileStorage')

    def test1(self):
        '''test basemodel object saving method'''
        my_model = BaseModel()
        my_model.save()
        self.assertIn('BaseModel.{}'.format(
            my_model.id), storage.all().keys())

    def test_pep8(self):
        '''pep8 styling'''
        check = 'Found code style errors'
        f = pep8.StyleGuide(quiet=True)
        fde = f.check_files(
            ['./models/engine/file_storage.py',
                'tests/test_models/test_engine/test_file_storage.py'])
        self.assertEqual(fde.total_errors, 0, check)

    def test_json(self):
        '''test Json'''
        my_model = BaseModel()
        my_model.name = 'Holberton'
        my_model.save()
        with open('file.json', 'r') as f:
            json_loaded = json.load(f)
        self.assertIn('BaseModel.{}'.format(
            my_model.id), json_loaded)


if __name__ == '__main__':
    unittest.main()
