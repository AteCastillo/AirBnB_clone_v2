#!/usr/bin/python3
"""Tests File"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import pep8
from datetime import datetime
import models


class TestAmenity(unittest.TestCase):
    """Test of Amenity class"""

    def test_Amenity(self):
        """Test instance of amenity class"""
        new = Amenity()
        new2 = Amenity()
        self.assertIsInstance(new, BaseModel)
        self.assertNotEqual(new, new2)
        self.assertNotEqual(new.id, new2.id)
        self.assertEqual(issubclass(new.__class__, BaseModel), True)
        self.assertIs(type(new), Amenity)
        self.assertTrue(hasattr(new, "id"))
        self.assertEqual(new.__str__(), "[{}] ({}) {}".format
                                        (new.__class__.__name__,
                                         new.id, new.__dict__))
        self.assertEqual(type(new.id), str)
        self.assertEqual(Amenity, type(Amenity()))

    def test_Amenity_init(self):
        new = Amenity(id="123", created_at="2021-02-17T22:46:38.883036",
                      updated_at="2021-02-17T22:46:38.883036")
        new2 = Amenity(id="123", name="Matias tu papi")
        self.assertFalse(hasattr(new2, "created_at"))
        self.assertTrue(hasattr(new2, "name"))
        self.assertEqual(new.id, "123")
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)

    def test_public_attr(self):
        """Test if the attributes are publics"""
        self.assertEqual(str, type(Amenity().id))
        self.assertEqual(datetime, type(Amenity().created_at))
        self.assertEqual(datetime, type(Amenity().updated_at))
        self.assertEqual(str, type(Amenity.name))

    def test_attr(self):
        new = Amenity()
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertTrue(hasattr(new, "name"))

    def test_documentation(self):
        """Check documentation"""
        self.assertIsNotNone(Amenity.__doc__)
        self.assertIsNotNone(Amenity.__init__.__doc__)
        self.assertIsNotNone(Amenity.save.__doc__)
        self.assertIsNotNone(Amenity.to_dict.__doc__)

    def test_pep8(self):
        """test pep8 comes back clean"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "pep8")

    def test_method_str(self):
        """Test method str"""
        new = Amenity()
        self.assertEqual(new.__str__(), "[{}] ({}) {}".format
                                        (new.__class__.__name__,
                                         new.id, new.__dict__))
        self.assertTrue(type(new.__str__()), str)
        self.assertTrue(len(new.__str__()))

    def test_to_dict(self):
        new = Amenity()
        dict_new = new.to_dict()
        self.assertNotEqual(new.__dict__, new.to_dict())
        self.assertEqual(type(dict_new["created_at"]), str)
        self.assertEqual(type(dict_new["updated_at"]), str)
        self.assertTrue("__class__" in dict_new)
        self.assertEqual(dict_new["__class__"],  "Amenity")

    def test_save(self):
        new = Amenity()
        created = new.updated_at
        new.save()
        updated = new.updated_at
        self.assertNotEqual(updated, created)
        self.assertGreater(updated, created)


if __name__ == "__main__":
    unittest.main()
