# encoding: utf-8
from __future__ import print_function

import json
import pytest

from nepal.models.container import Container
from nepal.models.node import Node
from profile.models.user import User

from toolbox.icepick import ordered


@pytest.mark.django_db
class ContainerTest:
    @pytest.fixture(autouse=True)
    def setUp(self, client):
        self.client = client
        self.user = User.objects.create_user(email='test@evt.com', password='test123')
        response = self.client.post('/users/login', data={'email': 'test@evt.com',
                                    'password': 'test123'})
        token = response.data.get('token')
        self.headers = {'HTTP_AUTHORIZATION': 'JWT {0}'.format(token)}

        node1 = {
            'name': 'node1',
            'so': 'centos',
            'provider': 'do',
            'ip': '104.10.232.13',
            'username': 'root',
            'password': 'root123'
        }
        self.node = Node.objects.create(**node1)
        container1 = {
            'id': 100,
            'name': 'container1',
            'config': {}
        }
        self.container = Container.objects.create(**container1)
        self.container.nodes.add(self.node)

    @pytest.mark.django_db(transaction=True)
    def test_create_new_container(self):
        data = {
            'name': 'container_test',
            'nodes': [self.node.id],
            'config': {
                "registry": {
                    "image": "registry:2.4",
                    "environment": [
                        "RACK_ENV=development",
                        "SHOW=true",
                        "DEBUG=False"
                    ],
                    "volumes": [
                        "/opt/registry/tmp:/tmp/registry-dev:Z",
                        "/opt/nginx/certs:/certs:Z"
                    ],
                    "expose": [
                        5000
                    ],
                    "ports": [
                        "5000:5000"
                    ]
                }
            }
        }

        result = self.client.post('/containers', data=json.dumps(data),
                                  content_type='application/json', **self.headers)
        # TODO: must be assert more things
        assert 201 == result.status_code

        result_db = Container.objects.get(name='container_test')
        assert 'container_test' == result_db.name
        assert ordered(data.get('config')) == ordered(result_db.config)

    @pytest.mark.xfail
    @pytest.mark.django_db(transaction=True)
    def test_start_a_container(self):
        response = self.client.get('/conteiners/1/?action=start',
                                   content_type='application/json', **self.headers)
        assert {} == response.data

    @pytest.mark.django_db(transaction=True)
    def test_get_container_all(self):
        response = self.client.get('/containers',
                                   content_type='application/json', **self.headers)
        assert 1 == len(response.data)

    @pytest.mark.django_db(transaction=True)
    def test_get_container_by_id(self):
        response = self.client.get('/containers/100', content_type='application/json',
                                   **self.headers)
        result = response.data

        assert 200 == response.status_code
        assert 100 == result.get('id')

    @pytest.mark.django_db(transaction=True)
    def test_update_container_ok(self):
        data = {
            'name': 'app1',
            'nodes': [self.node.id],
            'config': {
                "registry": {
                    "image": "registry:2.4",
                    "environment": [
                        "RACK_ENV=development",
                        "SHOW=true",
                        "DEBUG=False"
                    ],
                    "expose": [
                        5000
                    ],
                    "ports": [
                        "5000:5000"
                    ]
                }
            }
        }

        response = self.client.put('/containers/100', data=json.dumps(data),
                                   content_type='application/json', **self.headers)

        assert 200 == response.status_code

    @pytest.mark.django_db(transaction=True)
    def test_try_update_container_not_found(self):
        response = self.client.put('/containers/132', data=json.dumps({}),
                                   content_type='application/json', **self.headers)
        assert 404 == response.status_code

    @pytest.mark.django_db(transaction=True)
    def test_delete_container_ok(self):
        response = self.client.delete('/containers/100', content_type='application/json',
                                      **self.headers)
        assert 204 == response.status_code

    @pytest.mark.django_db(transaction=True)
    def test_try_delete_container_that_not_exist(self):
        response = self.client.delete('/containers/122', content_type='application/json',
                                      **self.headers)
        assert 404 == response.status_code
