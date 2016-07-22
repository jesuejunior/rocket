# encoding: utf-8
from __future__ import print_function

import json

import pytest
from engine.models.node import Node


@pytest.fixture(scope='class')
def setUp(request):
	node1 = {
		'id': 1,
		'name': 'node1',
		'so': 'ubuntu',
		'provider': 'vmware',
		'ip': '192.168.1.250',
		'username': 'admin',
		'password': 'abc123'
	}

	def tearDown():
		pass
	request.addfinalizer(tearDown)


def test_create_new_node(setUp, client):
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

def test_get_node_by_id(setUp, client):
	req = client.get('/nodes/1')
	result = json.loads(req.data).get('data')

	assert 200 == req.status_code
	assert 1 == result.get('id')
	assert 'node1' == result.get('name')
	assert 'vmware' == result.get('provider')
	assert '192.168.1.250' == result.get('ip')
	assert 'admin' == result.get('username')
	assert 'abc123' == result.get('password')

def test_update_node_ok(setUp, client):
	data = {
		'name': 'node100',
		'so': 'centos7',
		'provider': 'rackspace',
		'ip': '201.18.1.100',
	}

	req = client.put('/nodes/1', data=json.dumps(data), headers={'Content-Type': 'application/json'})

	# result = json.loads(req.data).get('data')

	assert 200 == req.status_code

	node = {}
	# assert 'node100' == node.name
	# assert 'centos7' == node.so
	# assert 'rackspace' == node.provider
	# assert '201.18.1.100' == str(node.ip)
	assert True

def test_delete_node_ok(setUp, client):
	result = client.delete('/nodes/1', headers={'Content-Type': 'application/json'})
	assert 204 == result.status_code
