#!/usr/bin/python3
""" define the unittest for state.py """
import models
import unittest
import os
from datetime import datetime
from time import sleep
from models.state import State


class TestState_saave(unittest.TestCase):
    """Unittests for testing save method of the State class."""

    @classmethod
    def ssetUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDownn(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_saave(self):
        stx = State()

        sleep(0.05)
        first_updated_at = stx.updated_at
        stx.save()
        self.assertLess(first_updated_at, stx.updated_at)

    def test_two_saaves(self):
        stx = State()

        sleep(0.05)
        first_updated_at = stx.updated_at
        stx.save()
        second_updated_at = stx.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        stx.save()
        self.assertLess(second_updated_at, stx.updated_at)

    def test_ssave_with_arg(self):
        stx = State()

        with self.assertRaises(TypeError):
            stx.save(None)

    def test_save_updatesfile(self):
        stx = State()
        stx.save()

        stid = "State." + stx.id
        with open("file.json", "r") as f:
            self.assertIn(stid, f.read())


class TestState_iinstantion(unittest.TestCase):
    """Unittests for testing instantiation of the State class."""

    def test_no_args_instantiat(self):

        self.assertEqual(State, type(State()))

    def test_new_instance_stored_in_objs(self):

        self.assertIn(State(), models.storage.all().values())

    def test_id_is_pl_str(self):

        self.assertEqual(str, type(State().id))

    def test_created_at_public_datetime(self):

        self.assertEqual(datetime, type(State().created_at))

    def test_updated_atpublic_datetime(self):

        self.assertEqual(datetime, type(State().updated_at))

    def test_name_public_class_attribute(self):
        stx = State()

        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(stx))
        self.assertNotIn("name", stx.__dict__)

    def test_two_states_uniq_ids(self):
        stx1 = State()
        stx2 = State()

        self.assertNotEqual(stx1.id, stx2.id)

    def test_two_states_diff_created_at(self):
        stx1 = State()
        sleep(0.05)
        stx2 = State()

        self.assertLess(stx1.created_at, stx2.created_at)

    def test_two_states_diff_updated_at(self):
        stx1 = State()
        sleep(0.05)
        stx2 = State()

        self.assertLess(stx1.updated_at, stx2.updated_at)

    def test_str_rep(self):
        dt = datetime.today()
        dt_repr = repr(dt)

        stx = State()
        stx.id = "123456"
        stx.created_at = stx.updated_at = dt
        ststr = stx.__str__()

        self.assertIn("[State] (123456)", ststr)
        self.assertIn("'id': '123456'", ststr)
        self.assertIn("'created_at': " + dt_repr, ststr)
        self.assertIn("'updated_at': " + dt_repr, ststr)

    def test_arg_unused(self):
        stx = State(None)

        self.assertNotIn(None, stx.__dict__.values())

    def test_instant_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()

        stx = State(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(stx.id, "345")
        self.assertEqual(stx.created_at, dt)
        self.assertEqual(stx.updated_at, dt)

    def test_instant_with_None_kwargs(self):
        with self.assertRaises(TypeError):

            State(id=None, created_at=None, updated_at=None)


class TestStatee_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the State class."""

    def test_too_dict_type(self):

        self.assertTrue(dict, type(State().to_dict()))

    def test_too_dict_contains_correct_keys(self):
        stx = State()

        self.assertIn("id", stx.to_dict())
        self.assertIn("created_at", stx.to_dict())
        self.assertIn("updated_at", stx.to_dict())
        self.assertIn("__class__", stx.to_dict())

    def test_to_dict_contains_added_attrs(self):
        stx = State()
        stx.middle_name = "Holberton"
        stx.my_number = 98

        self.assertEqual("Holberton", stx.middle_name)
        self.assertIn("my_number", stx.to_dict())

    def test_to_dict_datetime_attributes_strs(self):
        stx = State()
        st_dict = stx.to_dict()

        self.assertEqual(str, type(st_dict["id"]))
        self.assertEqual(str, type(st_dict["created_at"]))
        self.assertEqual(str, type(st_dict["updated_at"]))

    def test_to_d_output(self):
        dt = datetime.today()

        stx = State()
        stx.id = "123456"
        stx.created_at = stx.updated_at = dt
        tdict = {
                'id': '123456',
                '__class__': 'State',
                'created_at': dt.isoformat(),
                'updated_at': dt.isoformat(),
                }
        self.assertDictEqual(stx.to_dict(), tdict)

    def test_contrast_to_dunder_dict(self):
        stx = State()

        self.assertNotEqual(stx.to_dict(), stx.__dict__)

    def test_to_d_with_arg(self):
        stx = State()

        with self.assertRaises(TypeError):
            stx.to_dict(None)


if __name__ == "__main__":
    unittest.main()
