# encoding: utf-8
from __future__ import print_function

import json
import pytest
from model_mommy import mommy

from engine.models import Container


@pytest.fixture
def setUp(request):
	container1 = {
		'id': 1,
		'name': 'container1',
		'config': {}
	}

	mommy.make_one(Container, **container1)
	mommy.make_many(Container, 9)
	def tearDown():
		pass
	request.addfinalizer(tearDown)


@pytest.mark.django_db
def test_create_new_container(setUp, client):
	data = {
		'name': 'container_test',
		'config': {}

	}

	result = client.post('/containers', data=json.dumps(data), content_type='application/json', headers={'Content-Type': 'application/json'})
	# TODO: must be assert more things
	assert 201 == result.status_code
	assert 'centos' == result.data.get('so')

@pytest.mark.django_db
def test_get_container_all(setUp, client):
	req = client.get('/containers', headers={'Content-Type': 'application/json'} )
	assert 10 == len(req.data)

@pytest.mark.django_db
def test_get_container_by_id(setUp, client):
	req = client.get('/containers/1', headers={'Content-Type': 'application/json'} )
	result = req.data

	assert 200 == req.status_code
	assert 1 == result.get('id')


@pytest.mark.django_db
def test_update_container_ok(setUp, client):
	data = {
		'name': 'container1',
		'config': {}
	}

	req = client.put('/containers/1', data=json.dumps(data), content_type='application/json', headers={'Content-Type': 'application/json'})
	result = req.data

	assert 200 == req.status_code

@pytest.mark.django_db
def test_try_update_container_not_found(setUp, client):
	req = client.put('/containers/132', data=json.dumps({}), content_type='application/json', headers={'Content-Type': 'application/json'})

	assert 404 == req.status_code

@pytest.mark.django_db
def test_delete_container_ok(setUp, client):
	result = client.delete('/containers/1', headers={'Content-Type': 'application/json'})
	assert 204 == result.status_code

@pytest.mark.django_db
def test_try_delete_container_that_not_exist(setUp, client):
	result = client.delete('/containers/122', headers={'Content-Type': 'application/json'})
	assert 404 == result.status_code
