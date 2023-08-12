#!/usr/bin/python3
""" define the unittests for base.model """
import models
import unittest
import os
from time import sleep
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel_too_dictt(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_d_typee(self):
        bmx = BaseModel()

        self.assertTrue(dict, type(bmx.to_dict()))

    def test_to_d_contains_correct_keyys(self):
        bmx = BaseModel()

        self.assertIn("id", bmx.to_dict())
        self.assertIn("created_at", bmx.to_dict())
        self.assertIn("updated_at", bmx.to_dict())
        self.assertIn("__class__", bmx.to_dict())

    def test_to_d_contains_add_attributes(self):
        bmx = BaseModel()

        bmx.name = "Holberton"
        bmx.my_number = 98
        self.assertIn("name", bmx.to_dict())
        self.assertIn("my_number", bmx.to_dict())

    def test_to_d_datetime_attributes_strs(self):
        bmx = BaseModel()
        bmx_dict = bmx.to_dict()

        self.assertEqual(str, type(bmx_dict["created_at"]))
        self.assertEqual(str, type(bmx_dict["updated_at"]))

    def test_to_dictoutput(self):
        dtx = datetime.today()
        bmx = BaseModel()
        bmx.id = "123456"

        bmx.created_at = bmx.updated_at = dtx
        tdict = {
                'id': '123456',
                '__class__': 'BaseModel',
                'created_at': dtx.isoformat(),
                'updated_at': dtx.isoformat()
                }
        self.assertDictEqual(bmx.to_dict(), tdict)

    def test_contrast_to_d_dunderdict(self):
        bmx = BaseModel()

        self.assertNotEqual(bmx.to_dict(), bmx.__dict__)

    def test_to_dict_witharg(self):
        bmx = BaseModel()

        with self.assertRaises(TypeError):
            bmx.to_dict(None)


class TestBaseModel_iinstantiationn(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_noargs_instantiates(self):

        self.assertEqual(BaseModel, type(BaseModel()))

    def test_newinstance_stored_in_objects(self):

        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_ispublic_str(self):

        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_ispublic_datetime(self):

        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_ispublic_datetime(self):

        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        bmx1 = BaseModel()
        bmx2 = BaseModel()

        self.assertNotEqual(bmx1.id, bmx2.id)

    def test_two_models_differentcreated_at(self):
        bmx1 = BaseModel()
        sleep(0.05)
        bmx2 = BaseModel()

        self.assertLess(bmx1.created_at, bmx2.created_at)

    def test_two_models_differentupdated_at(self):
        bmx1 = BaseModel()
        sleep(0.05)
        bmx2 = BaseModel()

        self.assertLess(bmx1.updated_at, bmx2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        bmx = BaseModel()
        bmx.id = "123456"
        bmx.created_at = bmx.updated_at = dt
        bmstr = bmx.__str__()

        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)

    def test_argss_unused(self):
        bmx = BaseModel(None)

        self.assertNotIn(None, bmx.__dict__.values())

    def test_instantiation_withkwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()

        bmx = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bmx.id, "345")
        self.assertEqual(bmx.created_at, dt)
        self.assertEqual(bmx.updated_at, dt)

    def test_instantiation_with_Nonekwargs(self):
        with self.assertRaises(TypeError):

            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()

        bmx = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bmx.id, "345")
        self.assertEqual(bmx.created_at, dt)
        self.assertEqual(bmx.updated_at, dt)


class TestBaseModel_ssave(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    @classmethod
    def settUp(self):
        try:
            os.rename("file.json", "tmp")

        except IOError:
            pass

    @classmethod
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
        bmx = BaseModel()
        sleep(0.05)
        first_updated_at = bmx.updated_at
        bmx.save()

        self.assertLess(first_updated_at, bmx.updated_at)

    def test_two_ssaves(self):
        bmx = BaseModel()
        sleep(0.05)
        first_updated_at = bmx.updated_at
        bmx.save()
        second_updated_at = bmx.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        bmx.save()

        self.assertLess(second_updated_at, bmx.updated_at)

    def test_save_witharg(self):
        bmx = BaseModel()

        with self.assertRaises(TypeError):
            bmx.save(None)

    def test_sv_updates_file(self):
        bmx = BaseModel()
        bmx.save()

        bmid = "BaseModel." + bmx.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())


if __name__ == "__main__":
    unittest.main()
