# encoding: utf-8
import os
from flask import Flask
from flask_restful import Api

from engine.resources.container import ContainerResource
from engine.resources.deploy import DeployResource
from engine.resources.server import ServerResource


app = Flask(__name__)
app.config.from_object(__name__)

api = Api(app)

# Deploy endpoints
api.add_resource(DeployResource, '/deploy/new',)

# Container endpoints
api.add_resource(ContainerResource, '/container/all',)

# Server endpoints
api.add_resource(ServerResource, '/server/<int:id>')



