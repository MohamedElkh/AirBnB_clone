#!/usr/bin/python3
""" define the unittest for review.py """
import unittest
import os
import models
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_saave(unittest.TestCase):
    """Unittests for testing save method of the Review class."""

    @classmethod
    def seetUp(self):
        try:
            os.rename("file.json", "tmp")

        except IOError:
            pass

    def teearDown(self):
        try:
            os.remove("file.json")

        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")

        except IOError:
            pass

    def test_one_ssave(self):
        rvx = Review()

        sleep(0.05)
        first_updated_at = rvx.updated_at
        rvx.save()
        self.assertLess(first_updated_at, rvx.updated_at)

    def test_two_ssaves(self):
        rvx = Review()

        sleep(0.05)
        first_updated_at = rvx.updated_at
        rvx.save()
        second_updated_at = rvx.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        rvx.save()
        self.assertLess(second_updated_at, rvx.updated_at)

    def test_save_witharg(self):
        rvx = Review()

        with self.assertRaises(TypeError):
            rvx.save(None)

    def test_save_updatesfile(self):
        rvx = Review()
        rvx.save()
        rvid = "Review." + rvx.id

        with open("file.json", "r") as f:
            self.assertIn(rvid, f.read())


class TestReview_too_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Review class."""

    def test_to_dicttype(self):

        self.assertTrue(dict, type(Review().to_dict()))

    def test_to_dictcontains_correct_keys(self):
        rvx = Review()

        self.assertIn("id", rvx.to_dict())
        self.assertIn("created_at", rvx.to_dict())
        self.assertIn("updated_at", rvx.to_dict())
        self.assertIn("__class__", rvx.to_dict())

    def test_to_dict_contains_added(self):
        rvx = Review()

        rvx.middle_name = "Holberton"
        rvx.my_number = 98
        self.assertEqual("Holberton", rvx.middle_name)
        self.assertIn("my_number", rvx.to_dict())

    def test_to_dict_datetime_attributesarestrs(self):
        rvx = Review()

        rv_dict = rvx.to_dict()
        self.assertEqual(str, type(rv_dict["id"]))
        self.assertEqual(str, type(rv_dict["created_at"]))
        self.assertEqual(str, type(rv_dict["updated_at"]))

    def test_to_dictoutput(self):
        dt = datetime.today()
        rvx = Review()

        rvx.id = "123456"
        rvx.created_at = rvx.updated_at = dt
        tdict = {
                'id': '123456',
                '__class__': 'Review',
                'created_at': dt.isoformat(),
                'updated_at': dt.isoformat(),
                }
        self.assertDictEqual(rvx.to_dict(), tdict)

    def test_contrast_to_dict_dunderdict(self):
        rvx = Review()

        self.assertNotEqual(rvx.to_dict(), rvx.__dict__)

    def test_to_witharg(self):
        rvx = Review()

        with self.assertRaises(TypeError):
            rvx.to_dict(None)


class TestRevieww_instantiaation(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

    def test_no_argsinstantiates(self):

        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_inobjects(self):

        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_publicstr(self):

        self.assertEqual(str, type(Review().id))

    def test_created_at_public_datetime(self):

        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_public_datetime(self):

        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_public_class_attribute(self):
        rvx = Review()

        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rvx))
        self.assertNotIn("place_id", rvx.__dict__)

    def test_user_id_public_class_attribute(self):
        rvx = Review()

        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rvx))
        self.assertNotIn("user_id", rvx.__dict__)

    def test_text_is_public_class(self):
        rvx = Review()

        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rvx))
        self.assertNotIn("text", rvx.__dict__)

    def test_two_review_uniqueids(self):
        rvx1 = Review()
        rvx2 = Review()

        self.assertNotEqual(rvx1.id, rvx2.id)

    def test_two_reviews_dfferentcreated_at(self):
        rvx1 = Review()
        sleep(0.05)
        rvx2 = Review()

        self.assertLess(rvx1.created_at, rvx2.created_at)

    def test_two_review_differentupdated_at(self):
        rvx1 = Review()
        sleep(0.05)
        rvx2 = Review()

        self.assertLess(rvx1.updated_at, rvx2.updated_at)

    def test_str_representat(self):
        dt = datetime.today()
        dt_repr = repr(dt)

        rvx = Review()
        rvx.id = "123456"
        rvx.created_at = rvx.updated_at = dt
        rvstr = rvx.__str__()

        self.assertIn("[Review] (123456)", rvstr)
        self.assertIn("'id': '123456'", rvstr)
        self.assertIn("'created_at': " + dt_repr, rvstr)
        self.assertIn("'updated_at': " + dt_repr, rvstr)

    def test_argunused(self):
        rvx = Review(None)

        self.assertNotIn(None, rvx.__dict__.values())

    def test_instantiationwithkwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()

        rvx = Review(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(rvx.id, "345")
        self.assertEqual(rvx.created_at, dt)
        self.assertEqual(rvx.updated_at, dt)

    def test_instantiation_None_kwargs(self):
        with self.assertRaises(TypeError):

            Review(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
