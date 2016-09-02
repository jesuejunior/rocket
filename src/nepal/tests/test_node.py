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
        mommy.make_one(User, email='test@adm.cc', password='test123')
        
        token = client.post('/users/login', 
            data={'email': 'test@adm.cc', 'password': 'test123'})
        import ipdb; ipdb.set_trace()

        self.headers={'Content-Type': 'application/json',
                'Authorization': 'JWT {0}'.format(token['token'])}
        
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
    def test_create_new_node(self, client):
        data = {
            'name': 'node_test',
            'so': 'centos',
            'provider': 'aws',
            'ip': '192.168.1.100',
            'fqdn': 'node.foo.com',
            'username': 'admin2',
            'password': 'abc1234'
        }

        result = client.post('/nodes', data=json.dumps(data), headers=self.headers)
        # TODO: must be assert more things
        assert 201 == result.status_code
        assert 'centos' == result.data.get('so')

    @pytest.mark.django_db(transaction=True)
    def test_get_node_all(self, client):
        req = client.get('/nodes', headers=self.headers )
        assert 10 == len(req.data)

    @pytest.mark.django_db(transaction=True)
    def test_get_node_by_id(self, client):
        req = client.get('/nodes/1', headers=self.headers )
        result = req.data

        assert 200 == req.status_code
        assert 1 == result.get('id')
        assert 'node1' == result.get('name')
        assert 'vmware' == result.get('provider')
        assert '192.168.1.250' == result.get('ip')
        assert 'admin' == result.get('username')
        assert 'abc123' == result.get('password')

    @pytest.mark.django_db(transaction=True)
    def test_update_node_ok(self, client):
        data = {
            'name': 'node1',
            'so': 'centos7',
            'provider': 'do',
            'ip': '201.18.1.100',
            'fqdn': 'node.bar.com',
            'username': 'admin',
            'password': 'cba123'
        }

        req = client.put('/nodes/1', data=json.dumps(data), headers=self.headers)
        result = req.data

        assert 200 == req.status_code
        assert 'node1' == result.get('name')
        assert 'centos7' == result.get('so')
        assert 'do' == result.get('provider')
        assert '201.18.1.100' == str(result.get('ip'))

    @pytest.mark.django_db(transaction=True)
    def test_try_update_node_not_found(self, client):
        req = client.put('/nodes/132', data=json.dumps({}), headers=self.headers)
        assert 404 == req.status_code

    @pytest.mark.django_db(transaction=True)
    def test_delete_node_ok(self, client):
        result = client.delete('/nodes/1', headers=self.headers)
        assert 204 == result.status_code

    @pytest.mark.django_db(transaction=True)
    def test_try_delete_node_that_not_exist(self, client):
        result = client.delete('/nodes/122', headers=self.headers)
        assert 404 == result.status_code
