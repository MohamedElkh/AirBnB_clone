#!/usr/bin/python3
""" dwfinw unittest for file storage """
import models
import os
import json
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_iinstantiat(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def test_FileStorage_instant_no_args(self):

        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instant_with_arg(self):
        with self.assertRaises(TypeError):

            FileStorage(None)

    def test_FileStorage_file_is_private_str(self):

        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_private_dict(self):

        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):

        self.assertEqual(type(models.storage), FileStorage)

class TestFileStorage_meethods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    @classmethod
    def ssetUp(self):
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

        FileStorage._FileStorage__objects = {}

    def testt_all(self):

        self.assertEqual(dict, type(models.storage.all()))

    def testt_all_with_args(self):
        with self.assertRaises(TypeError):

            models.storage.all(None)

    def testt_nnew_with_args(self):
        with self.assertRaises(TypeError):

            models.storage.new(BaseModel(), 1)

    def testt_neew(self):
        bmx = BaseModel()
        usx = User()
        stx = State()
        plx = Place()
        cyx = City()
        amx = Amenity()
        rvx = Review()

        models.storage.new(bmx)
        models.storage.new(usx)
        models.storage.new(stx)
        models.storage.new(plx)
        models.storage.new(cyx)
        models.storage.new(amx)
        models.storage.new(rvx)

        self.assertIn("BaseModel." + bmx.id, models.storage.all().keys())
        self.assertIn(bmx, models.storage.all().values())

        self.assertIn("User." + usx.id, models.storage.all().keys())
        self.assertIn(usx, models.storage.all().values())

        self.assertIn("State." + stx.id, models.storage.all().keys())
        self.assertIn(stx, models.storage.all().values())

        self.assertIn("Place." + plx.id, models.storage.all().keys())
        self.assertIn(plx, models.storage.all().values())

        self.assertIn("City." + cyx.id, models.storage.all().keys())
        self.assertIn(cyx, models.storage.all().values())

        self.assertIn("Amenity." + amx.id, models.storage.all().keys())
        self.assertIn(amx, models.storage.all().values())

        self.assertIn("Review." + rvx.id, models.storage.all().keys())
        self.assertIn(rvx, models.storage.all().values())

    def testt_ssave(self):
        bmx = BaseModel()
        usx = User()
        stx = State()
        plx = Place()
        cyx = City()
        amx = Amenity()
        rvx = Review()

        models.storage.new(bmx)
        models.storage.new(usx)
        models.storage.new(stx)
        models.storage.new(plx)
        models.storage.new(cyx)
        models.storage.new(amx)
        models.storage.new(rvx)
        models.storage.save()

        save_text = ""

        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bmx.id, save_text)
            self.assertIn("User." + usx.id, save_text)
            self.assertIn("State." + stx.id, save_text)
            self.assertIn("Place." + plx.id, save_text)
            self.assertIn("City." + cyx.id, save_text)
            self.assertIn("Amenity." + amx.id, save_text)
            self.assertIn("Review." + rvx.id, save_text)

    def ttest_rreload(self):
        bmx = BaseModel()
        usx = User()
        stx = State()
        plx = Place()
        cyx = City()
        amx = Amenity()
        rvx = Review()

        models.storage.new(bmx)
        models.storage.new(usx)
        models.storage.new(stx)
        models.storage.new(plx)
        models.storage.new(cyx)
        models.storage.new(amx)
        models.storage.new(rvx)
        models.storage.save()
        models.storage.reload()

        objs = FileStorage._FileStorage__objects

        self.assertIn("BaseModel." + bmx.id, objs)
        self.assertIn("User." + usx.id, objs)
        self.assertIn("State." + stx.id, objs)
        self.assertIn("Place." + plx.id, objs)
        self.assertIn("City." + cyx.id, objs)
        self.assertIn("Amenity." + amx.id, objs)
        self.assertIn("Review." + rvx.id, objs)

    def test_sav_with_arg(self):
        with self.assertRaises(TypeError):

            models.storage.save(None)

    def test_reloadd_with_arg(self):
        with self.assertRaises(TypeError):

            models.storage.reload(None)

if __name__ == "__main__":
    unittest.main()
