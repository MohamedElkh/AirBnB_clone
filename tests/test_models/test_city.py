#!/usr/bin/python3
""" define the unittests for city """
import os
import models
from datetime import datetime
from time import sleep
from models.city import City
import unittest


class TestCity_savee(unittest.TestCase):
    """Unittests for testing save method of the City class."""

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

    def test_one_ssave(self):
        cyx = City()
        sleep(0.05)
        first_updated_at = cyx.updated_at
        cyx.save()

        self.assertLess(first_updated_at, cyx.updated_at)

    def test_two_savess(self):
        cyx = City()
        sleep(0.05)
        first_updated_at = cyx.updated_at
        cyx.save()

        second_updated_at = cyx.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        cyx.save()
        self.assertLess(second_updated_at, cyx.updated_at)

    def test_save_witharg(self):
        cyx = City()

        with self.assertRaises(TypeError):
            cyx.save(None)

    def test_save_updatesfile(self):
        cyx = City()
        cyx.save()
        cyid = "City." + cyx.id

        with open("file.json", "r") as f:
            self.assertIn(cyid, f.read())


class TestCity_instantiatioon(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    def test_no_args_instantat(self):

        self.assertEqual(City, type(City()))

    def test_new_instance_stored_objs(self):

        self.assertIn(City(), models.storage.all().values())

    def test_id_public_str(self):

        self.assertEqual(str, type(City().id))

    def test_created_at_publc_datetime(self):

        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_publc_datetime(self):

        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_public_class_attrs(self):
        cyx = City()

        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(cyx))
        self.assertNotIn("state_id", cyx.__dict__)

    def test_name_public_class_attrs(self):
        cyx = City()

        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(cyx))
        self.assertNotIn("name", cyx.__dict__)

    def test_two_citiesunique_ids(self):
        cyx1 = City()
        cyx2 = City()

        self.assertNotEqual(cyx1.id, cyx2.id)

    def test_two_cities_diff_created_at(self):
        cyx1 = City()
        sleep(0.05)
        cyx2 = City()

        self.assertLess(cyx1.created_at, cyx2.created_at)

    def test_two_cities_differnt_updated_at(self):
        cyx1 = City()
        sleep(0.05)
        cyx2 = City()

        self.assertLess(cyx1.updated_at, cyx2.updated_at)

    def test_str_represntation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        cyx = City()
        cyx.id = "123456"
        cyx.created_at = cyx.updated_at = dt
        cystr = cyx.__str__()

        self.assertIn("[City] (123456)", cystr)
        self.assertIn("'id': '123456'", cystr)
        self.assertIn("'created_at': " + dt_repr, cystr)
        self.assertIn("'updated_at': " + dt_repr, cystr)

    def test_arg_unused(self):
        cyx = City(None)

        self.assertNotIn(None, cyx.__dict__.values())

    def test_instantiation_with_kwarg(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        cyx = City(id="345", created_at=dt_iso, updated_at=dt_iso)

        self.assertEqual(cyx.id, "345")
        self.assertEqual(cyx.created_at, dt)
        self.assertEqual(cyx.updated_at, dt)

    def test_instantiation_withNone_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCity_too_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the City class."""

    def test_too_dict_type(self):

        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_contain_correct_keys(self):
        cyx = City()

        self.assertIn("id", cyx.to_dict())
        self.assertIn("created_at", cyx.to_dict())
        self.assertIn("updated_at", cyx.to_dict())
        self.assertIn("__class__", cyx.to_dict())

    def test_to_dict_contains_addedattributes(self):
        cyx = City()

        cyx.middle_name = "Holberton"
        cyx.my_number = 98
        self.assertEqual("Holberton", cyx.middle_name)
        self.assertIn("my_number", cyx.to_dict())

    def test_to_dict_datetime_attributes_strs(self):
        cyx = City()
        cy_dict = cyx.to_dict()

        self.assertEqual(str, type(cy_dict["id"]))
        self.assertEqual(str, type(cy_dict["created_at"]))
        self.assertEqual(str, type(cy_dict["updated_at"]))

    def test_too_dict_output(self):
        dt = datetime.today()
        cyx = City()
        cyx.id = "123456"
        cyx.created_at = cyx.updated_at = dt

        tdict = {
                'id': '123456',
                '__class__': 'City',
                'created_at': dt.isoformat(),
                'updated_at': dt.isoformat(),
                }
        self.assertDictEqual(cyx.to_dict(), tdict)

    def test_contrast_to_dict_dnder_dict(self):
        cyx = City()

        self.assertNotEqual(cyx.to_dict(), cyx.__dict__)

    def test_to_dict_witharg(self):
        cyx = City()

        with self.assertRaises(TypeError):
            cyx.to_dict(None)


if __name__ == "__main__":
    unittest.main()
