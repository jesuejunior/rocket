# encoding: utf-8
from __future__ import print_function
import unittest
import json

from alchemytools.context import managed

from engine.models import Metadata, Session
from engine.models.server import Server
from rocket.settings import app


class ServerTest(unittest.TestCase):

	def setUp(self):
		Metadata.drop_all()
		Metadata.create_all()
		self.app = app.test_client()

		self.server1 = {
			'id': 1,
			'name': 'server1',
			'so': 'ubuntu',
			'provider': 'vmware',
			'ip': '192.168.1.250',
			'username': 'admin',
			'password': 'abc123'
		}

		with managed(Session) as session:
			server = Server(**self.server1)
			session.add(server)

	def tearDown(self):
		Metadata.drop_all()
		print("Finish up")

	def test_create_new_server(self):

		data = {
			'name': 'server_test',
			'so': 'ubuntu',
			'provider': 'aws',
			'ip': '192.168.1.100',
			'username': 'admin',
			'password': 'abc123'
		}

		srv = self.app.post('/server', data=json.dumps(data), headers={'Content-Type':'application/json'})

		assert srv.data == data

	def test_get_server_by_id(self):
		rv = self.app.get('/server/1')
		assert '123' == rv.data