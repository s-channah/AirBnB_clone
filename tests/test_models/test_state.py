#!/usr/bin/env python3
"""
Unit Test Model to the state class
"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """
    Class to test state
    """
    def test_state_attr(self):
        """
        Test of the state instancr hass all required attributes
        """
        state = State()
        self.assertIsInstance(state, State)
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))
        self.assertTrue(hasattr(state, 'name'))

    def test_state_atrr_access(self):
        """
        This method tests the user attriubutes can be accessed when inti
        """
        state = State()
        state.name = "Tours"

        self.assertEqual(state.name, "Tours")

    def test_user_str_rep(self):
        """
        This method rtest if the inputs of user are of type string
        """

        state = State()
        state.name = "Orlean"

        standard_output = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(str(state), standard_output)


if __name__ == '__main__':
    unittest.main()
