#!/usr/bin/python3
""" Unittests for models/base_model.py """
import os
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """ Unittests for the testing of instantiation of the BaseModel class """

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        m = BaseModel()
        m.id = "718293"
        m.created_at = m.updated_at = dt
        mstr = m.__str__()
        self.assertIn("[BaseModel] (718293)", mstr)
        self.assertIn("'id': '718293'", mstr)
        self.assertIn("'created_at': " + dt_repr, mstr)
        self.assertIn("'updated_at': " + dt_repr, mstr)

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())
