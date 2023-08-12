#!/usr/bin/python3
""" test the console """
import unittest
import sys
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity
from models.base_model import BaseModel


class TestTheConsole(unittest.TestCase):
    """ this test for checks if all req class are created """
    def test_classes(self):
        """ this test checks if all req classes are created """
        cityyx = City()
        amenityyx = Amenity()
        stateex = State()
        revvx = Review()
        placeex = Place()

        self.assertEqual(cityyx.__class__.__name__, "City")
        self.assertEqual(amenityyx.__class__.__name__, "Amenity")
        self.assertEqual(stateex.__class__.__name__, "State")
        self.assertEqual(revvx.__class__.__name__, "Review")
        self.assertEqual(placeex.__class__.__name__, "Place")

    def test_parents(self):
        """ this test checks if all classs are inherit """
        cityyx = City()
        amenityyx = Amenity()
        stateex = State()
        revvx = Review()
        placeex = Place()

        self.assertTrue(issubclass(cityyx.__class__, BaseModel))
        self.assertTrue(issubclass(amenityyx.__class__, BaseModel))
        self.assertTrue(issubclass(stateex.__class__, BaseModel))
        self.assertTrue(issubclass(revvx.__class__, BaseModel))
        self.assertTrue(issubclass(placeex.__class__, BaseModel))
