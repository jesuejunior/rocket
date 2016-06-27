# encoding: utf-8
from __future__ import print_function

import json

import pytest
from alchemytools.context import managed

from engine.models.node import Node
from rocket import app
from rocket.settings import Metadata, Session


@pytest.fixture(scope='class')
def setUp(request):
	Metadata.drop_all()
	Metadata.create_all()

	node1 = {
		'id': 1,
		'name': 'node1',
		'so': 'ubuntu',
		'provider': 'vmware',
		'ip': '192.168.1.250',
		'username': 'admin',
		'password': 'abc123'
	}

	with managed(Session) as session:
		node = Node(**node1)
		session.add(node)
		session.commit()
	# app.run(host='0.0.0.0', port=8000)

	def tearDown():
		Metadata.drop_all()

	request.addfinalizer(tearDown)


def test_create_new_node(setUp):
	with app.test_client() as client:
		data = {
			'name': 'node_test',
			'so': 'centos',
			'provider': 'aws',
			'ip': '192.168.1.100',
			'fqdn': 'node.foo.com',
			'username': 'admin',
			'password': 'abc123'
		}

		result = client.post('/nodes', data=json.dumps(data), headers={'Content-Type': 'application/json'})

	assert 201 == result.status_code


def test_get_node_by_id(setUp):
	client = app.test_client()
	req = client.get('/nodes/1')
	result = json.loads(req.data).get('data')

	assert 200 == req.status_code
	assert 1 == result.get('id')
	assert 'node1' == result.get('name')
	assert 'vmware' == result.get('provider')
	assert '192.168.1.250' == result.get('ip')
	assert 'admin' == result.get('username')
	assert 'abc123' == result.get('password')


def test_update_node_ok(setUp):
	with app.test_client() as client:
		data = {
			'name': 'node100',
			'so': 'centos7',
			'provider': 'rackspace',
			'ip': '201.18.1.100',
		}

		req = client.put('/nodes/1', data=json.dumps(data), headers={'Content-Type': 'application/json'})

	# result = json.loads(req.data).get('data')

	assert 200 == req.status_code

	with managed(Session) as session:
		node = session.query(Node).get(1)
	assert 'node100' == node.name
	assert 'centos7' == node.so
	assert 'rackspace' == node.provider
	assert '201.18.1.100' == str(node.ip)


def test_delete_node_ok(setUp):
	with app.test_client() as client:
		result = client.delete('/nodes/1', headers={'Content-Type': 'application/json'})
	assert 204 == result.status_code
