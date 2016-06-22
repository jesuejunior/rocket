# encoding: utf-8
import os
from flask import Flask
from flask_restful import Api

from engine.resources.container import ContainerResource
from engine.resources.deploy import DeployResource
from engine.resources.node import NodeResource


app = Flask(__name__)
app.config.from_object(__name__)


api = Api(app)

api_version = 'v1'
