#!/usr/bin/python3
"""Tests File"""
import unittest
from models.state import State
from models.base_model import BaseModel
import pep8
from datetime import datetime
import models


class TestState(unittest.TestCase):
    """Test of State class"""

    def test_State(self):
        """Test instance of amenity class"""
        new = State()
        new2 = State()
        self.assertIsInstance(new, BaseModel)
        self.assertEqual(issubclass(new.__class__, BaseModel), True)
        self.assertIs(type(new), State)
        self.assertTrue(hasattr(new, "id"))
        self.assertNotEqual(new, new2)
        self.assertNotEqual(new.id, new2.id)
        self.assertEqual(new.__str__(), "[{}] ({}) {}".format
                                        (new.__class__.__name__,
                                         new.id, new.__dict__))
        self.assertEqual(type(new.id), str)
        self.assertEqual(State, type(State()))
        #

    def test_check_in_storage(self):
        """Check if the instance is in __objects"""
        self.assertIn(State(), models.storage.all().values())

    def test_public_attr(self):
        """Test if the attributes are publics"""
        self.assertEqual(str, type(State().id))
        self.assertEqual(datetime, type(State().created_at))
        self.assertEqual(datetime, type(State().updated_at))
        self.assertEqual(str, type(State.name))

    def test_State_init(self):
        """Test Init with Kwargs"""
        new = State(id="123", created_at="2021-02-17T22:46:38.883036",
                    updated_at="2021-02-17T22:46:38.883036")
        new2 = State(id="123", name="Matias tu papi")
        self.assertFalse(hasattr(new2, "created_at"))
        self.assertTrue(hasattr(new2, "name"))
        self.assertEqual(new.id, "123")
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)

    def test_attr(self):
        new = State()
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertTrue(hasattr(new, "name"))
        self.assertFalse(hasattr(new, "state_id"))
        self.assertEqual(type(new.name), str)
        self.assertNotEqual(type(new.name), int)
        self.assertNotEqual(type(new.name), list)

    def test_documentation(self):
        """Check documentation"""
        self.assertIsNotNone(State.__doc__)
        self.assertIsNotNone(State.__init__.__doc__)
        self.assertIsNotNone(State.save.__doc__)
        self.assertIsNotNone(State.to_dict.__doc__)

    def test_pep8(self):
        """test pep8 comes back clean"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/State.py'])
        self.assertEqual(result.total_errors, 0, "pep8")

    def test_method_str(self):
        """Test method str"""
        new = State()
        self.assertEqual(new.__str__(), "[{}] ({}) {}".format
                                        (new.__class__.__name__,
                                         new.id, new.__dict__))
        self.assertTrue(type(new.__str__()), str)
        self.assertTrue(len(new.__str__()))

    def test_to_dict(self):
        new = State()
        dict_new = new.to_dict()
        self.assertNotEqual(new.__dict__, new.to_dict())
        self.assertEqual(type(dict_new["created_at"]), str)
        self.assertEqual(type(dict_new["updated_at"]), str)
        self.assertTrue("__class__" in dict_new)
        self.assertEqual(dict_new["__class__"],  "State")

    def test_save(self):
        new = State()
        created = new.updated_at
        new.save()
        updated = new.updated_at
        self.assertNotEqual(updated, created)
        self.assertGreater(updated, created)


if __name__ == "__main__":
    unittest.main()
