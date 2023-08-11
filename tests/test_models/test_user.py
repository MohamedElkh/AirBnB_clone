#!/usr/bin/python3
""" define the unittest for user.py """
import models
import os
import unittest
from time import sleep
from models.user import User
from datetime import datetime


class TestUser_save(unittest.TestCase):
    """Unittests for testing save method of the  class."""

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

    def test_one_saave(self):
        usx = User()

        sleep(0.05)
        first_updated_at = usx.updated_at
        usx.save()
        self.assertLess(first_updated_at, usx.updated_at)

    def test_two_saaves(self):
        usx = User()

        sleep(0.05)
        first_updated_at = usx.updated_at
        usx.save()
        second_updated_at = usx.updated_at

        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        usx.save()
        self.assertLess(second_updated_at, usx.updated_at)

    def test_save_with_arrg(self):
        usx = User()

        with self.assertRaises(TypeError):
            usx.save(None)

    def test_saave_updates_file(self):
        usx = User()
        usx.save()

        usid = "User." + usx.id
        with open("file.json", "r") as f:
            self.assertIn(usid, f.read())


class TestUser_instantiatiion(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""

    def test_no_args_instan(self):

        self.assertEqual(User, type(User()))

    def test_new_stored_in_objects(self):

        self.assertIn(User(), models.storage.all().values())

    def test_id_is_pubc_str(self):

        self.assertEqual(str, type(User().id))

    def test_created_at_public_datetime(self):

        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_public_datetime(self):

        self.assertEqual(datetime, type(User().updated_at))

    def test_email_public_str(self):

        self.assertEqual(str, type(User.email))

    def test_passwd_is_public_str(self):

        self.assertEqual(str, type(User.password))

    def test_firt_name_public_str(self):

        self.assertEqual(str, type(User.first_name))

    def test_last_name_public_str(self):

        self.assertEqual(str, type(User.last_name))

    def test_two_users_unique_ids(self):
        usx1 = User()
        usx2 = User()

        self.assertNotEqual(usx1.id, usx2.id)

    def test_two_users_diff_created_at(self):
        usx1 = User()
        sleep(0.05)
        usx2 = User()

        self.assertLess(usx1.created_at, usx2.created_at)

    def test_two_users_diff_updated_at(self):
        usx1 = User()
        sleep(0.05)
        usx2 = User()

        self.assertLess(usx1.updated_at, usx2.updated_at)

    def test_str_represent(self):
        dt = datetime.today()
        dt_repr = repr(dt)

        usx = User()
        usx.id = "123456"
        usx.created_at = usx.updated_at = dt

        usstr = usx.__str__()
        self.assertIn("[User] (123456)", usstr)
        self.assertIn("'id': '123456'", usstr)
        self.assertIn("'created_at': " + dt_repr, usstr)
        self.assertIn("'updated_at': " + dt_repr, usstr)

    def test_args_uunused(self):
        usx = User(None)

        self.assertNotIn(None, usx.__dict__.values())

    def test_instantiation_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()

        usx = User(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(usx.id, "345")
        self.assertEqual(usx.created_at, dt)
        self.assertEqual(usx.updated_at, dt)

    def test_instantiation_None_kwargs(self):
        with self.assertRaises(TypeError):

            User(id=None, created_at=None, updated_at=None)


class TestUser_to_dictt(unittest.TestCase):
    """Unittests for testing to_dict method of the User class."""

    def test_to_dicttype(self):

        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_contain_correct_key(self):
        usx = User()

        self.assertIn("id", usx.to_dict())
        self.assertIn("created_at", usx.to_dict())
        self.assertIn("updated_at", usx.to_dict())
        self.assertIn("__class__", usx.to_dict())

    def test_to_dict_contains_added_attribs(self):
        usx = User()
        usx.middle_name = "Holberton"
        usx.my_number = 98

        self.assertEqual("Holberton", usx.middle_name)
        self.assertIn("my_number", usx.to_dict())

    def test_to_dict_datetime_attrs_are_strs(self):
        usx = User()
        us_dict = usx.to_dict()

        self.assertEqual(str, type(us_dict["id"]))
        self.assertEqual(str, type(us_dict["created_at"]))
        self.assertEqual(str, type(us_dict["updated_at"]))

    def test_to_d_output(self):
        dt = datetime.today()
        usx = User()
        usx.id = "123456"
        usx.created_at = usx.updated_at = dt

        tdict = {
                'id': '123456',
                '__class__': 'User',
                'created_at': dt.isoformat(),
                'updated_at': dt.isoformat(),
                }
        self.assertDictEqual(usx.to_dict(), tdict)

    def test_contrast_to_d_dunder_dict(self):
        usx = User()

        self.assertNotEqual(usx.to_dict(), usx.__dict__)

    def test_to_dict_arg(self):
        usx = User()

        with self.assertRaises(TypeError):
            usx.to_dict(None)


if __name__ == "__main__":
    unittest.main()
