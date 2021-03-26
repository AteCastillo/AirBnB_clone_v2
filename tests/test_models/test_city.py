#!/usr/bin/python3
"""Tests File"""
import unittest
from models.city import City
from models.base_model import BaseModel
from datetime import datetime
import models
import pep8


class TestCity(unittest.TestCase):
    """Test of City class"""

    def test_City(self):
        """Test instance of city class"""
        new = City()
        new2 = City()
        self.assertIsInstance(new, BaseModel)
        self.assertEqual(issubclass(new.__class__, BaseModel), True)
        self.assertIs(type(new), City)
        self.assertNotEqual(new, new2)
        self.assertNotEqual(new.id, new2.id)
        self.assertEqual(new.__str__(), "[{}] ({}) {}".format
                                        (new.__class__.__name__,
                                         new.id, new.__dict__))
        self.assertEqual(type(new.id), str)
        self.assertEqual(City, type(City()))

    def test_City_init(self):
        """Test Init with Kwargs"""
        new = City(id="123", created_at="2021-02-17T22:46:38.883036",
                   updated_at="2021-02-17T22:46:38.883036")
        new2 = City(id="123", name="Matias tu papi")
        self.assertFalse(hasattr(new2, "created_at"))
        self.assertTrue(hasattr(new2, "name"))
        self.assertEqual(new.id, "123")
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

    def test_public_attr(self):
        """Test if the attributes are publics"""
        self.assertEqual(str, type(City().id))
        self.assertEqual(datetime, type(City().created_at))
        self.assertEqual(datetime, type(City().updated_at))
        self.assertEqual(str, type(City.name))
        self.assertEqual(str, type(City.state_id))

    def test_attr(self):
        new = City()
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertTrue(hasattr(new, "state_id"))
        self.assertTrue(hasattr(new, "name"))

    def test_documentation(self):
        """Check documentation"""
        self.assertIsNotNone(City.__doc__)
        self.assertIsNotNone(City.__init__.__doc__)
        self.assertIsNotNone(City.save.__doc__)
        self.assertIsNotNone(City.to_dict.__doc__)

    def test_pep8(self):
        """test pep8 comes back clean"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "pep8")

    def test_method_str(self):
        """Test method str"""
        new = City()
        self.assertEqual(new.__str__(), "[{}] ({}) {}".format
                                        (new.__class__.__name__,
                                         new.id, new.__dict__))
        self.assertTrue(type(new.__str__()), str)
        self.assertTrue(len(new.__str__()))

    def test_to_dict(self):
        new = City()
        dict_new = new.to_dict()
        self.assertNotEqual(new.__dict__, new.to_dict())
        self.assertEqual(type(dict_new["created_at"]), str)
        self.assertEqual(type(dict_new["updated_at"]), str)
        self.assertTrue("__class__" in dict_new)
        self.assertEqual(dict_new["__class__"],  "City")

    def test_save(self):
        new = City()
        created = new.updated_at
        new.save()
        updated = new.updated_at
        self.assertNotEqual(updated, created)
        self.assertGreater(updated, created)


if __name__ == "__main__":
    unittest.main()
