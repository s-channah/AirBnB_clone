#!/usr/bin/env python3
"""
Unit Test Model to the user class
"""
import unittest
from models.base_model import BaseModel
from models.user import User

class TestUser(unittest.TestCase):
    """
    Class to test user
    """
    def test_user_attr(self):
        """
        Test of the user instancr hass all required attributes
        """
        user = User()
        self.assertIsInstance(user, User)
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_user_atrr_access(self):
        """
        This method tests the user attriubutes can be accessed when inti
        """
        user = User()
        user.email = "topservices@gmail.com"
        user.password = "HGJfsgs$&"
        user.first_name = "Desmond"
        user.last_name = "Elliot"

        self.assertEqual(user.email, "topservices@gmail.com")
        self.assertEqual(user.password, "HGJfsgs$&")
        self.assertEqual(user.first_name, "Desmond")
        self.assertEqual(user.last_name, "Elliot")

    def test_user_str_rep(self):
        """
        This method rtest if the inputs of user are of type string
        """

        user = User()
        user.email = "topsevices@gmail.com"
        user.password = "oiuhqijsdfpjpofaksqôskjbhbq"
        user.last_name = "Glide"
        user.first_name = "Descent"

        standard_output = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(str(user), standard_output)

if __name__ == '__main__':
    unittest.main()

