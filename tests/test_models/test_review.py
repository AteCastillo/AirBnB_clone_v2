#!/usr/bin/python3
"""Tests File"""
import unittest
from models.review import Review
from models.base_model import BaseModel
import pep8
from datetime import datetime
import models


class TestReview(unittest.TestCase):
    """Test of Review class"""

    def test_Review(self):
        """Test instance of amenity class"""
        new = Review()
        new2 = Review()
        self.assertIsInstance(new, BaseModel)
        self.assertEqual(issubclass(new.__class__, BaseModel), True)
        self.assertIs(type(new), Review)
        self.assertTrue(hasattr(new, "id"))
        self.assertNotEqual(new, new2)
        self.assertNotEqual(new.id, new2.id)
        self.assertEqual(new.__str__(), "[{}] ({}) {}".format
                                        (new.__class__.__name__,
                                         new.id, new.__dict__))
        self.assertEqual(type(new.id), str)
        self.assertEqual(Review, type(Review()))

    def test_Review_init(self):
        """Test Init with Kwargs"""
        new = Review(id="123", created_at="2021-02-17T22:46:38.883036",
                        updated_at="2021-02-17T22:46:38.883036")
        new2 = Review(id="123", name="Matias tu papi")
        self.assertFalse(hasattr(new2, "created_at"))
        self.assertTrue(hasattr(new2, "name"))
        self.assertEqual(new.id, "123")
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

    def test_public_attr(self):
        """Test if the attributes are publics"""
        self.assertEqual(str, type(Review().id))
        self.assertEqual(datetime, type(Review().created_at))
        self.assertEqual(datetime, type(Review().updated_at))
        self.assertEqual(str, type(Review.place_id))
        self.assertEqual(str, type(Review.user_id))
        self.assertEqual(str, type(Review.text))

    def test_attr(self):
        new = Review()
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertTrue(hasattr(new, "place_id"))
        self.assertTrue(hasattr(new, "user_id"))
        self.assertTrue(hasattr(new, "text"))
        self.assertNotEqual(type(new.place_id), int)
        self.assertNotEqual(type(new.place_id), list)
        self.assertEqual(type(new.place_id), str)
        self.assertNotEqual(type(new.user_id), list)
        self.assertNotEqual(type(new.user_id), int)
        self.assertEqual(type(new.user_id), str)
        self.assertNotEqual(type(new.text), list)
        self.assertNotEqual(type(new.text), int)
        self.assertEqual(type(new.text), str)

    def test_documentation(self):
        """Check documentation"""
        self.assertIsNotNone(Review.__doc__)
        self.assertIsNotNone(Review.__init__.__doc__)
        self.assertIsNotNone(Review.save.__doc__)
        self.assertIsNotNone(Review.to_dict.__doc__)

    def test_pep8(self):
        """test pep8 comes back clean"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, "pep8")

    def test_method_str(self):
        """Test method str"""
        new = Review()
        self.assertEqual(new.__str__(), "[{}] ({}) {}".format
                                        (new.__class__.__name__,
                                         new.id, new.__dict__))
        self.assertTrue(type(new.__str__()), str)
        self.assertTrue(len(new.__str__()))

    def test_to_dict(self):
        new = Review()
        dict_new = new.to_dict()
        self.assertNotEqual(new.__dict__, new.to_dict())
        self.assertEqual(type(dict_new["created_at"]), str)
        self.assertEqual(type(dict_new["updated_at"]), str)
        self.assertTrue("__class__" in dict_new)
        self.assertEqual(dict_new["__class__"],  "Review")

    def test_save(self):
        new = Review()
        created = new.updated_at
        new.save()
        updated = new.updated_at
        self.assertNotEqual(updated, created)
        self.assertGreater(updated, created)


if __name__ == "__main__":
    unittest.main()
