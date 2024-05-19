#!/usr/bin/env python3
"""
Unit Test Model to the user class
"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """
    Class to test city
    """
    def test_city_attr(self):
        """
        Test of the city instancr hass all required attributes
        """
        city = City()
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")

    def test_city_inherits_from_base_model(self):
        """
        This method tests that the city class instance inherits from
        from the BaseModel
        """
        city = City()
        self.assertTrue(isinstance(city, BaseModel))

    def test_city_args_correct(self):
        """
        This method tests the amenity init with args
        """
        city = City(name="Tours", state_id="37")
        self.assertEqual(city.name, "Tours")
        self.assertEqual(city.state_id, "37")


if __name__ == '__main__':
    unittest.main()
