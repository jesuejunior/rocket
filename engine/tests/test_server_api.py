# encoding: utf-8
from __future__ import print_function
import pytest
import json

from alchemytools.context import managed

from engine.models import Metadata, Session
from engine.models.server import Server
from rocket.settings import app


@pytest.fixture(scope='function')
def setUp(request):
	client = app.test_client()

	server1 = {
		'id': 1,
		'name': 'server1',
		'so': 'ubuntu',
		'provider': 'vmware',
		'ip': '192.168.1.250',
		'username': 'admin',
		'password': 'abc123'
	}

	with managed(Session) as session:
		server = Server(**server1)
		session.add(server)

	def tearDown(self):
		Metadata.drop_all()
		Metadata.create_all()
		print("Finish up")

	request.addfinalizer(tearDown)

	def test_create_new_server(setUp):

		data = {
			'name': 'server_test',
			'so': 'ubuntu',
			'provider': 'aws',
			'ip': '192.168.1.100',
			'fqdn': 'server.foo.com',
			'username': 'admin',
			'password': 'abc123'
		}

		srv = client.app.post('/v1/servers', data=json.dumps(data), headers={'Content-Type':'application/json'})

		assert srv.data == data

	def test_get_server_by_id(setUp):
		req = client.app.get('/v1/servers/1')
		result = json.loads(req.data)
		assert 1 == result.get('id')