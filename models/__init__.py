#!/usr/bin/env python3
"""
This is the initialisation file for the model templates
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
