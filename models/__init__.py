#!/usr/bin/python3
"""Contains initialization code for the models package"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
