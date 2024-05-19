#!/usr/bin/env python3
"""
Unit Test Model to the user class
"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Class to test user
    """
    def test_amenity_attr(self):
        """
        Test of the amenity instancr hass all required attributes
        """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_amenity_inherits_from_base_model(self):
        """
        This method tests that the amenity class instance inherits from
        from the BaseModel
        """
        amenity = Amenity()
        self.assertTrue(isinstance(amenity, BaseModel))

    def test_amenity_args_correct(self):
        """
        This method tests the amenity init with args
        """
        amenity = Amenity(name="Pool")
        self.assertEqual(amenity.name, "Pool")


if __name__ == '__main__':
    unittest.main()
