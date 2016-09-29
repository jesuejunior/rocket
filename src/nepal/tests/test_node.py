# encoding: utf-8
from __future__ import print_function

import json
import pytest
from model_mommy import mommy

from nepal.models.node import Node
from profile.models.user import User


@pytest.mark.django_db
class NodeTest:
    @pytest.fixture(autouse=True)
    def setUp(self, client):
        self.client = client
        self.user = User.objects.create_user(email='test@adm.cc', password='test123')
        self.headers = {'Content-Type': 'application/json'}
        response = self.client.post('/users/login', headers=self.headers,
            data={'email': 'test@adm.cc', 'password': 'test123'})

        token = response.data.get('token')
        # self.auth = {'Authorization': 'JWT {0}'.format(token)}
        self.headers.update({'HTTP_AUTHORIZATION': 'JWT {0}'.format(token)})
        node1 = {
            'id': 100,
            'name': 'node1',
            'so': 'ubuntu',
            'provider': 'vmware',
            'ip': '192.168.1.250',
            'username': 'admin',
            'password': 'abc123'
        }

        mommy.make_one(Node, **node1)
        mommy.make_many(Node, 9)

    @pytest.mark.django_db(transaction=True)
    def test_try_get_nodes_without_auth(self):
        response = self.client.get('/nodes', content_type='application/json')
        assert 401 == response.status_code

    @pytest.mark.django_db(transaction=True)
    def test_create_new_node(self):
        data = {
            'name': 'node_test',
            'so': 'centos',
            'provider': 'aws',
            'ip': '192.168.1.100',
            'fqdn': 'node.foo.com',
            'username': 'admin2',
            'password': 'abc1234'
        }

        response = self.client.post('/nodes', data=json.dumps(data),
                content_type='application/json', **self.headers)
        # TODO: must be assert more things
        assert 201 == response.status_code
        assert 'centos' == response.data.get('so')

    @pytest.mark.django_db(transaction=True)
    def test_get_node_all(self):
        response = self.client.get('/nodes', **self.headers)
        assert 200 == response.status_code
        assert 10 == len(response.data)

    @pytest.mark.django_db(transaction=True)
    def test_get_node_by_id(self):
        response = self.client.get('/nodes/100', **self.headers)
        result = response.data

        assert 200 == response.status_code
        assert 100 == result.get('id')
        assert 'node1' == result.get('name')
        assert 'vmware' == result.get('provider')
        assert '192.168.1.250' == result.get('ip')
        assert 'admin' == result.get('username')
        assert 'abc123' == result.get('password')

    @pytest.mark.django_db(transaction=True)
    def test_update_node_ok(self):
        data = {
            'name': 'node1',
            'so': 'centos7',
            'provider': 'do',
            'ip': '201.18.1.100',
            'fqdn': 'node.bar.com',
            'username': 'admin',
            'password': 'cba123'
        }

        req = self.client.put('/nodes/100', data=json.dumps(data),
                content_type='application/json', **self.headers)
        result = req.data

        assert 200 == req.status_code
        assert 'node1' == result.get('name')
        assert 'centos7' == result.get('so')
        assert 'do' == result.get('provider')
        assert '201.18.1.100' == str(result.get('ip'))

    @pytest.mark.django_db(transaction=True)
    def test_try_update_node_not_found(self):
        response = self.client.put('/nodes/132', data=json.dumps({}),
                content_type='application/json', **self.headers)
        assert 404 == response.status_code

    @pytest.mark.django_db(transaction=True)
    def test_delete_node_ok(self):
        result = self.client.delete('/nodes/100', **self.headers)
        assert 204 == result.status_code

    @pytest.mark.django_db(transaction=True)
    def test_try_delete_node_that_not_exist(self):
        result = self.client.delete('/nodes/122', **self.headers)
        assert 404 == result.status_code
