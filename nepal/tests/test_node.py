# encoding: utf-8
from __future__ import print_function

import json
import pytest
from model_mommy import mommy

from nepal.models import Node


@pytest.fixture
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

	mommy.make_one(Node, **node1)
	mommy.make_many(Node, 9)
	def tearDown():
		pass
	request.addfinalizer(tearDown)


@pytest.mark.django_db
def test_create_new_node(setUp, client):
	data = {
		'name': 'node_test',
		'so': 'centos',
		'provider': 'aws',
		'ip': '192.168.1.100',
		'fqdn': 'node.foo.com',
		'username': 'admin2',
		'password': 'abc1234'
	}

	result = client.post('/nodes', data=json.dumps(data), content_type='application/json', headers={'Content-Type': 'application/json'})
	# TODO: must be assert more things
	assert 201 == result.status_code
	assert 'centos' == result.data.get('so')

@pytest.mark.django_db
def test_get_node_all(setUp, client):
	req = client.get('/nodes', headers={'Content-Type': 'application/json'} )
	assert 10 == len(req.data)

@pytest.mark.django_db
def test_get_node_by_id(setUp, client):
	req = client.get('/nodes/1', headers={'Content-Type': 'application/json'} )
	result = req.data

	assert 200 == req.status_code
	assert 1 == result.get('id')
	assert 'node1' == result.get('name')
	assert 'vmware' == result.get('provider')
	assert '192.168.1.250' == result.get('ip')
	assert 'admin' == result.get('username')
	assert 'abc123' == result.get('password')

@pytest.mark.django_db
def test_update_node_ok(setUp, client):
	data = {
		'name': 'node1',
		'so': 'centos7',
		'provider': 'do',
		'ip': '201.18.1.100',
		'fqdn': 'node.bar.com',
		'username': 'admin',
		'password': 'cba123'
	}

	req = client.put('/nodes/1', data=json.dumps(data), content_type='application/json', headers={'Content-Type': 'application/json'})
	result = req.data

	assert 200 == req.status_code
	assert 'node1' == result.get('name')
	assert 'centos7' == result.get('so')
	assert 'do' == result.get('provider')
	assert '201.18.1.100' == str(result.get('ip'))

@pytest.mark.django_db
def test_try_update_node_not_found(setUp, client):
	req = client.put('/nodes/132', data=json.dumps({}), content_type='application/json', headers={'Content-Type': 'application/json'})

	assert 404 == req.status_code

@pytest.mark.django_db
def test_delete_node_ok(setUp, client):
	result = client.delete('/nodes/1', headers={'Content-Type': 'application/json'})
	assert 204 == result.status_code

@pytest.mark.django_db
def test_try_delete_node_that_not_exist(setUp, client):
	result = client.delete('/nodes/122', headers={'Content-Type': 'application/json'})
	assert 404 == result.status_code
