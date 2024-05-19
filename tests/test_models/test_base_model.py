#!/usr/bin/env python3
"""
Base model unit testing script
"""

import unittest
import json
import uuid as generate_id
from datetime import datetime
import os
from models.base_model import BaseModel

global_update = None


class TestBaseModel(unittest.TestCase):
    """
    The class that handles the test of the BaseModel
    """

    def test_attr_presence(self):
        """
        This method checks that the attributes exists and assertained
        """
        tar = BaseModel()
        attributes = ["id", "created_at", "updated_at", "to_dict", "save"]
        self.assertTrue(all(hasattr(tar, attr) for attr in attributes))

    def test_date_values(self):
        """
        This method handles the correctness of the date values
        """
        new_class_inst = BaseModel().to_dict()
        new_inst_time = new_class_inst["created_at"][:20]
        self.assertEqual(new_inst_time, str(datetime.now().isoformat())[:20])

    def test_uuid_if_unique(self):
        """
        This method tests for the uniqueness of the UUID
        """
        new_class_inst = BaseModel()
        uuid = new_class_inst.id
        self.assertNotEqual(uuid, str(generate_id.uuid4()))

    def test_str_representation(self):
        """
        This is the method that tests for the str passed to json for stprage
        """
        new_class_inst = BaseModel()
        self.assertIsInstance(new_class_inst.__str__(), str)

    def test_save_method(self):
        """
        This method tests the SAVE
        """
        new_class_inst = BaseModel()
        time = new_class_inst.created_at
        self.assertEqual(time, new_class_inst.updated_at)
        new_class_inst.save()
        self.assertNotEqual(time, new_class_inst.updated_at)

    def test_init_with_kwargs(self):
        """
        This is methods checks a pass of kwargs
        and how it is impacted in the run
        """
        test_id = "{}".format(generate_id.uuid4())
        str_date_format = "{}".format(datetime.now().isoformat())
        non_iso_format = datetime.fromisoformat(str_date_format)
        base_data = {
                "__class__": "BaseModel",
                "updated_at": str_date_format,
                "created_at": str_date_format,
                "id": test_id
                }
        new_class_inst = BaseModel(**base_data)
        self.assertEqual(new_class_inst.id, test_id)
        self.assertEqual(new_class_inst.updated_at, non_iso_format)
        self.assertEqual(new_class_inst.created_at, non_iso_format)

    def test_none(self):
        """
        NULL
        """
        new_inst = BaseModel(None)
        attributes = ["id", "created_at", "updated_at", "to_dict", "save"]
        self.assertTrue(all(hassattr(new_inst, attr) for attr in attributes))


if __name__ == "__main__":
    unittest.main()
