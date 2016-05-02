# encoding: utf-8
import os
from flask import Flask
from flask_restful import Api

from engine.resources.container import ContainerResource
from engine.resources.deploy import DeployResource
from engine.resources.server import ServerResource

DB_USER = os.environ.get('DB_USER', 'rocket')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'rocket')
DB_HOST = os.environ.get('DB_HOST', '192.168.99.100')
DB_PORT = os.environ.get('DB_PORT', 5432)
DB_NAME = os.environ.get('DB_NAME', 'rocket')

TEST = os.environ.get('TEST', False)

app = Flask(__name__)
app.config.from_object(__name__)

api = Api(app)

# Deploy endpoints
api.add_resource(DeployResource, '/deploy/new',)

# Container endpoints
api.add_resource(ContainerResource, '/container/all',)

# Server endpoints
api.add_resource(ServerResource, '/server/<int:id>')



