#!/usr/bin/python3
"""Tests File"""
import unittest
import models
from models.user import User
from models.base_model import BaseModel
from datetime import datetime
import pep8


class TestUser(unittest.TestCase):
    """Test of User class"""

    def test_User(self):
        """Test instance of User class"""
        new = User()
        new2 = User()
        self.assertIsInstance(new, BaseModel)
        self.assertEqual(issubclass(new.__class__, BaseModel), True)
        self.assertIs(type(new), User)
        self.assertTrue(hasattr(new, "id"))
        self.assertNotEqual(new, new2)
        self.assertNotEqual(new.id, new2.id)
        self.assertEqual(new.__str__(), "[{}] ({}) {}".format
                                        (new.__class__.__name__,
                                         new.id, new.__dict__))
        self.assertEqual(type(new.id), str)
        self.assertIn(User(), models.storage.all().values())
        self.assertEqual(User, type(User()))
        self.assertEqual(str, type(User().id))
        self.assertEqual(datetime, type(User().created_at))
        self.assertEqual(datetime, type(User().updated_at))
        self.assertEqual(str, type(User.email))
        self.assertEqual(str, type(User.password))
        self.assertEqual(str, type(User.first_name))

    def test_User_init(self):
        """Test Init with Kwargs"""
        new = User(id="123", created_at="2021-02-17T22:46:38.883036",
                   updated_at="2021-02-17T22:46:38.883036")
        new2 = User(name="Matias tu papi")
        self.assertFalse(hasattr(new2, "id"))
        self.assertFalse(hasattr(new2, "created_at"))
        self.assertFalse(hasattr(new2, "updated_at"))
        self.assertTrue(hasattr(new2, "name"))
        self.assertEqual(new.id, "123")
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)
        new3 = User(1234)
        self.assertEqual(type(new3).__name__, "User")
        self.assertFalse(hasattr(new3, "1234"))

    def test_attr(self):
        """Test attributes"""
        new = User()
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertTrue(hasattr(new, "email"))
        self.assertEqual(type(new.email), str)
        self.assertNotEqual(type(new.email), int)
        self.assertNotEqual(type(new.email), list)

    def test_documentation(self):
        """Check documentation"""
        self.assertIsNotNone(User.__doc__)
        self.assertIsNotNone(User.__init__.__doc__)
        self.assertIsNotNone(User.__str__.__doc__)
        self.assertIsNotNone(User.save.__doc__)
        self.assertIsNotNone(User.to_dict.__doc__)

    def test_pep8(self):
        """test pep8 comes back clean"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, "pep8")

    def test_method_str(self):
        """Test method str"""
        new = User()
        self.assertEqual(new.__str__(), "[{}] ({}) {}".format
                                        (new.__class__.__name__,
                                         new.id, new.__dict__))
        self.assertTrue(type(new.__str__()), str)
        self.assertTrue(len(new.__str__()))

    def test_to_dict(self):
        new = User()
        dict_new = new.to_dict()
        self.assertNotEqual(new.__dict__, new.to_dict())
        self.assertEqual(type(dict_new["created_at"]), str)
        self.assertEqual(type(dict_new["updated_at"]), str)
        self.assertTrue("__class__" in dict_new)
        self.assertEqual(dict_new["__class__"],  "User")

    def test_save(self):
        new = User()
        created = new.updated_at
        new.save()
        updated = new.updated_at
        self.assertNotEqual(updated, created)
        self.assertGreater(updated, created)


if __name__ == "__main__":
    unittest.main()
