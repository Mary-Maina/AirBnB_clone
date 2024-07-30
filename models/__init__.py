#!/usr/bin/python3
"""
Executes once models are imported
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
