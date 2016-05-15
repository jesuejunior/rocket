# encoding: utf-8
from __future__ import print_function

import json

import pytest
from alchemytools.context import managed

from engine.models import Metadata, Session
from engine.models.server import Server
from rocket.settings import app


@pytest.fixture(scope='class')
def setUp(request):
	Metadata.drop_all()
	Metadata.create_all()

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
		session.commit()

	def tearDown():
		Metadata.drop_all()

	request.addfinalizer(tearDown)


def test_create_new_server(setUp):
	with app.test_client() as client:
		data = {
			'name': 'server_test',
			'so': 'centos',
			'provider': 'aws',
			'ip': '192.168.1.100',
			'fqdn': 'server.foo.com',
			'username': 'admin',
			'password': 'abc123'
		}

		result = client.post('/v1/servers', data=json.dumps(data), headers={'Content-Type':'application/json'})

	assert 201 == result.status_code


def test_get_server_by_id(setUp):
	client = app.test_client()
	req = client.get('/v1/servers/1')
	result = json.loads(req.data).get('data')

	assert 200 == req.status_code
	assert 1 == result.get('id')
	assert 'server1' == result.get('name')
	assert 'vmware' == result.get('provider')
	assert '192.168.1.250' == result.get('ip')
	assert 'admin' == result.get('username')
	assert 'abc123' == result.get('password')


def test_update_server_ok(setUp):
	with app.test_client() as client:
		data = {
			'name': 'server100',
			'so': 'centos7',
			'provider': 'rackspace',
			'ip': '201.18.1.100',
		}

		req = client.put('/v1/servers/1', data=json.dumps(data), headers={'Content-Type':'application/json'})

	# result = json.loads(req.data).get('data')

	assert 200 == req.status_code

	with managed(Session) as session:
		server = session.query(Server).get(1)
	assert 'server100' == server.name
	assert 'centos7' == server.so
	assert 'rackspace' == server.provider
	assert '201.18.1.100' == str(server.ip)

def test_delete_server_ok(setUp):
	with app.test_client() as client:
		result = client.delete('/v1/servers/1', headers={'Content-Type':'application/json'})
	assert 204 == result.status_code

