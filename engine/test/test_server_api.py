# encoding: utf-8
import unittest

from engine.models import Metadata
from rocket.settings import app


class ServerTest(unittest.TestCase):

	def setUp(self):
		self.app = app.test_client()
		Metadata.drop_all()
		Metadata.create_all()

	def tearDown(self):
		print("Finish up")

	def test_get_server_by_id(self):
		rv = self.app.get('/server/1')
		assert '' in rv.data
