#!/usr/bin/python3
""" define unittests fro amenity """
from datetime import datetime
from time import sleep
import os
import models
import unittest
from models.amenity import Amenity


class TestAmenity_save(unittest.TestCase):
    """Unittests for testing save method of the Amenity class."""

    @classmethod
    def ssetUp(self):
        try:
            os.rename("file.json", "tmp")

        except IOError:
            pass

    def tearrDown(self):
        try:
            os.remove("file.json")

        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_savee(self):
        amx = Amenity()

        sleep(0.05)
        first_updated_at = amx.updated_at
        amx.save()
        self.assertLess(first_updated_at, amx.updated_at)

    def test_two_savves(self):
        amx = Amenity()

        sleep(0.05)
        first_updated_at = amx.updated_at
        amx.save()
        second_updated_at = amx.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        amx.save()
        self.assertLess(second_updated_at, amx.updated_at)

    def test_save_witharg(self):
        amx = Amenity()

        with self.assertRaises(TypeError):
            amx.save(None)

    def test_save_updatesfile(self):
        amx = Amenity()
        amx.save()

        amid = "Amenity." + amx.id
        with open("file.json", "r") as f:
            self.assertIn(amid, f.read())


class TestAmenity_instantiatioon(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def test_no_args_iinstantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_iinstance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_ppublic_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_ppublic_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_ppublic_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_classattribute(self):
        amx = Amenity()

        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", amx.__dict__)

    def test_two_amenitiess_unique_ids(self):
        amx1 = Amenity()
        amx2 = Amenity()

        self.assertNotEqual(amx1.id, amx2.id)

    def test_two_amenities_different_ccreated_at(self):
        amx1 = Amenity()
        sleep(0.05)
        amx2 = Amenity()

        self.assertLess(amx1.created_at, amx2.created_at)

    def test_two_amenities_differnt_updated_at(self):
        amx1 = Amenity()
        sleep(0.05)
        amx2 = Amenity()

        self.assertLess(amx1.updated_at, amx2.updated_at)

    def test_str_representatioon(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        amx = Amenity()
        amx.id = "123456"
        amx.created_at = amx.updated_at = dt
        amstr = amx.__str__()

        self.assertIn("[Amenity] (123456)", amstr)
        self.assertIn("'id': '123456'", amstr)
        self.assertIn("'created_at': " + dt_repr, amstr)
        self.assertIn("'updated_at': " + dt_repr, amstr)

    def test_args_unused(self):
        amx = Amenity(None)

        self.assertNotIn(None, amx.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """instantiation with kwargs test method"""
        dt = datetime.today()
        dt_iso = dt.isoformat()

        amx = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(amx.id, "345")
        self.assertEqual(amx.created_at, dt)
        self.assertEqual(amx.updated_at, dt)

    def test_instantiation_none_kwargs(self):
        with self.assertRaises(TypeError):

            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_too_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Amenity class."""

    def test_to_dict_tyype(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        amx = Amenity()

        self.assertIn("id", amx.to_dict())
        self.assertIn("created_at", amx.to_dict())
        self.assertIn("updated_at", amx.to_dict())
        self.assertIn("__class__", amx.to_dict())

    def test_to_dict_contains_addedattributes(self):
        amx = Amenity()

        amx.middle_name = "Holberton"
        amx.my_number = 98
        self.assertEqual("Holberton", amx.middle_name)
        self.assertIn("my_number", amx.to_dict())

    def test_to_dict_datetime_attribut_are_strs(self):
        amx = Amenity()

        am_dict = amx.to_dict()
        self.assertEqual(str, type(am_dict["id"]))
        self.assertEqual(str, type(am_dict["created_at"]))
        self.assertEqual(str, type(am_dict["updated_at"]))

    def test_to_dictt_output(self):
        dt = datetime.today()
        amx = Amenity()
        amx.id = "123456"
        amx.created_at = amx.updated_at = dt

        tdict = {
                'id': '123456',
                '__class__': 'Amenity',
                'created_at': dt.isoformat(),
                'updated_at': dt.isoformat(),
                }
        self.assertDictEqual(amx.to_dict(), tdict)

    def test_contrast_to_dict_dnder_dict(self):
        amx = Amenity()

        self.assertNotEqual(amx.to_dict(), amx.__dict__)

    def test_to_dict_witharg(self):
        amx = Amenity()

        with self.assertRaises(TypeError):
            amx.to_dict(None)


if __name__ == "__main__":
    unittest.main()
