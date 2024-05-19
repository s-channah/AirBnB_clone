#!/usr/bin/env python3
"""
Unit Test Model to the state class
"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Class to test state
    """
    def rest_review_inherits_from_base_model(self):
        """
        Test that review inherits from base model
        """
        review = Review()
        self.assertTrue(isinstance(review, BaseModel))

    def test_review_attr(self):
        """
        Test of the state instancr hass all required attributes
        """
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_atrr_access(self):
        """
        This method tests the user attriubutes can be accessed when inti
        """
        review = Review(place_id="245", user_id="451", text="Review")
        self.assertEqual(review.place_id, "245")
        self.assertEqual(review.user_id, "451")
        self.assertEqual(review.text, "Review")

    def test_review_attr_types(self):
        """
        This method rtest if the inputs of user are of type string
        """

        review = Review()
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)


if __name__ == '__main__':
    unittest.main()
