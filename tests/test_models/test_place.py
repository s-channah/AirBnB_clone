#!/usr/bin/env python3
"""
Unit Test Model to the user class
"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Class to test user
    """
    def test_place_attr(self):
        """
        Test of the user instancr hass all required attributes
        """
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_per_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_place_inherits_from_base_model(self):
        """
        Test that the class Place inherits from BaseModel
        """
        place = Place()
        self.assertTrue(isinstance(place, BaseModel))

    def test_place_attr_access(self):
        """
        Test of the place instancr hass all required attributes
        """
        place = Place(city_id="37", user_id="451", name="Accord", description="Description",
                number_rooms=1, number_bathrooms=1, max_guest=2, price_per_night=100,
                latitude=3.124, longitude=32.124, ametity_ids=[0, 1, 2])
        self.assertEqual(place.city_id, "37")
        self.assertEqual(place.user_id, "451")
        self.assertEqual(place.name, "Accord")
        self.assertEqual(place.description, "Description")
        self.assertEqual(place.number_rooms, 1)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 2)
        self.assertEqual(place.price_per_night, 100)
        self.assertEqual(place.latitude, 3.124)
        self.assertEqual(place.longitude, 32.124)
        self.assertEqual(place.amenity_ids, [0, 1, 2])


if __name__ == '__main__':
    unittest.main()
