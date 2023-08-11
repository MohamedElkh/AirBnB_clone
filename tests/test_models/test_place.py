#!/usr/bin/python3
""" define the unittest for place.py """
import models
import unittest
import os
from time import sleep
from models.place import Place
from datetime import datetime


class TestPlace_too_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Place class."""

    def test_too_dict_type(self):

        self.assertTrue(dict, type(Place().to_dict()))

    def test_too_dict_contains_correct_keys(self):
        plx = Place()

        self.assertIn("id", plx.to_dict())
        self.assertIn("created_at", plx.to_dict())
        self.assertIn("updated_at", plx.to_dict())
        self.assertIn("__class__", plx.to_dict())

    def test_to_dict_contains_add_atributes(self):
        pxl = Place()

        pxl.middle_name = "Holberton"
        pxl.my_number = 98
        self.assertEqual("Holberton", pxl.middle_name)
        self.assertIn("my_number", pxl.to_dict())

    def test_to_dict_datetime_attributes_strs(self):
        pxl = Place()

        pl_dict = pxl.to_dict()
        self.assertEqual(str, type(pl_dict["id"]))
        self.assertEqual(str, type(pl_dict["created_at"]))
        self.assertEqual(str, type(pl_dict["updated_at"]))

    def test_to_dictt_output(self):
        dt = datetime.today()
        pxl = Place()
        pxl.id = "123456"
        pxl.created_at = pxl.updated_at = dt

        tdict = {
                'id': '123456',
                '__class__': 'Place',
                'created_at': dt.isoformat(),
                'updated_at': dt.isoformat(),
                }
        self.assertDictEqual(pxl.to_dict(), tdict)

    def test_contrast_to_dictdunder_dict(self):
        pxl = Place()

        self.assertNotEqual(pxl.to_dict(), pxl.__dict__)

    def test_to_dict_witharg(self):
        pxl = Place()

        with self.assertRaises(TypeError):
            pxl.to_dict(None)


class TestPlace_iinstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def test_no_argsinstantiat(self):

        self.assertEqual(Place, type(Place()))

    def test_new_instancestored_in_objects(self):

        self.assertIn(Place(), models.storage.all().values())

    def test_idis_public_str(self):

        self.assertEqual(str, type(Place().id))

    def test_created_atis_public_datetime(self):

        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_atis_public_datetime(self):

        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_idis_public_class_attribute(self):
        plx = Place()

        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(plx))
        self.assertNotIn("city_id", plx.__dict__)

    def test_user_id_is_public_class(self):
        plx = Place()

        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(plx))
        self.assertNotIn("user_id", plx.__dict__)

    def test_name_is_public_class_attribute(self):
        plx = Place()

        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(plx))
        self.assertNotIn("name", plx.__dict__)

    def test_description_is_public_class(self):
        plx = Place()

        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(plx))
        self.assertNotIn("desctiption", plx.__dict__)

    def test_number_rooms_is_public_class(self):
        plx = Place()

        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(plx))
        self.assertNotIn("number_rooms", plx.__dict__)

    def test_number_bathrooms_is_public_class(self):
        plx = Place()

        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(plx))
        self.assertNotIn("number_bathrooms", plx.__dict__)

    def test_max_guest_is_public_class(self):
        plx = Place()

        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(plx))
        self.assertNotIn("max_guest", plx.__dict__)

    def test_price_by_night_is_public_class(self):
        pxl = Place()

        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(pxl))
        self.assertNotIn("price_by_night", pxl.__dict__)

    def test_latitude_is_public_class(self):
        plx = Place()

        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(plx))
        self.assertNotIn("latitude", plx.__dict__)

    def test_longitude_is_public_class(self):
        plx = Place()

        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(plx))
        self.assertNotIn("longitude", plx.__dict__)

    def test_amenity_ids_is_public_class(self):
        plx = Place()

        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(plx))
        self.assertNotIn("amenity_ids", plx.__dict__)

    def test_two_places_uniqueids(self):
        plx1 = Place()
        plx2 = Place()

        self.assertNotEqual(plx1.id, plx2.id)

    def test_two_places_differentcreated_at(self):
        plx1 = Place()
        sleep(0.05)
        plx2 = Place()

        self.assertLess(plx1.created_at, plx2.created_at)

    def test_two_places_differentupdated_at(self):
        plx1 = Place()
        sleep(0.05)
        plx2 = Place()

        self.assertLess(plx1.updated_at, plx2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        plx = Place()
        plx.id = "123456"
        plx.created_at = plx.updated_at = dt
        plstr = plx.__str__()

        self.assertIn("[Place] (123456)", plstr)
        self.assertIn("'id': '123456'", plstr)
        self.assertIn("'created_at': " + dt_repr, plstr)
        self.assertIn("'updated_at': " + dt_repr, plstr)

    def test_argsunused(self):
        plx = Place(None)

        self.assertNotIn(None, plx.__dict__.values())

    def test_instantiationwith_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()

        plx = Place(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(plx.id, "345")
        self.assertEqual(plx.created_at, dt)
        self.assertEqual(plx.updated_at, dt)

    def test_instantiation_withNone_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


class TestPlace_ssave(unittest.TestCase):
    """Unittests for testing save method of the Place class."""

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

    def test_onesaave(self):
        plx = Place()
        sleep(0.05)
        first_updated_at = plx.updated_at
        plx.save()

        self.assertLess(first_updated_at, plx.updated_at)

    def test_two_saaves(self):
        plx = Place()
        sleep(0.05)
        first_updated_at = plx.updated_at
        plx.save()

        second_updated_at = plx.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        plx.save()
        self.assertLess(second_updated_at, plx.updated_at)

    def test_save_witharg(self):
        plx = Place()

        with self.assertRaises(TypeError):
            plx.save(None)

    def test_save_updatesfile(self):
        plx = Place()
        plx.save()
        plid = "Place." + plx.id

        with open("file.json", "r") as f:
            self.assertIn(plid, f.read())


if __name__ == "__main__":
    unittest.main()
