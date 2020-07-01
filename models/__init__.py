#!/usr/bin/python3
'''construct module'''
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()