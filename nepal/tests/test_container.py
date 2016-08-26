# encoding: utf-8
from __future__ import print_function

import json
import pytest

from nepal.models import Container
from toolbox.icepick import ordered


@pytest.mark.django_db
class ContainerTest:
    @pytest.fixture(autouse=True)
    def setUp(request):
            container1 = {
                    'id': 1,
                    'name': 'container1',
                    'config': {}
            }

            Container.objects.create(**container1)

            def tearDown():
                    pass
            request.addfinalizer(tearDown)


    @pytest.mark.django_db(transaction=True)
    def test_create_new_container(self, client):
        data = {
            'name': 'container_test',
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

        result = client.post('/containers', data=json.dumps(data), content_type='application/json',
                headers={'Content-Type': 'application/json'})
        # TODO: must be assert more things
        assert 201 == result.status_code

        result_db = Container.objects.get(name='container_test')
        assert 'container_test' == result_db.name
        assert ordered(data.get('config')) == ordered(result_db.config)

    @pytest.mark.django_db(transaction=True)
    def test_start_a_container(self, client):
        req = client.get('/conteiners/1/?action=start', headers={'Content-Type': 'application/json'})
        assert {} == req.data

    @pytest.mark.django_db(transaction=True)
    def test_get_container_all(self, client):
            req = client.get('/containers', headers={'Content-Type': 'application/json'} )
            assert 1 == len(req.data)

    @pytest.mark.django_db(transaction=True)
    def test_get_container_by_id(self, client):
            req = client.get('/containers/1', headers={'Content-Type': 'application/json'} )
            result = req.data

            assert 200 == req.status_code
            assert 1 == result.get('id')


    @pytest.mark.django_db(transaction=True)
    def test_update_container_ok(self, client):
            data = {
                    'name': 'container1',
                    'config': {}
            }

            req = client.put('/containers/1', data=json.dumps(data), content_type='application/json', headers={'Content-Type': 'application/json'})

            assert 200 == req.status_code

    @pytest.mark.django_db(transaction=True)
    def test_try_update_container_not_found(self, client):
            req = client.put('/containers/132', data=json.dumps({}), content_type='application/json', headers={'Content-Type': 'application/json'})

            assert 404 == req.status_code

    @pytest.mark.django_db(transaction=True)
    def test_delete_container_ok(self, client):
            result = client.delete('/containers/1', headers={'Content-Type': 'application/json'})
            assert 204 == result.status_code

    @pytest.mark.django_db(transaction=True)
    def test_try_delete_container_that_not_exist(self, client):
            result = client.delete('/containers/122', headers={'Content-Type': 'application/json'})
            assert 404 == result.status_code

