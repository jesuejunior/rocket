# encoding: utf-8
import os
from flask import Flask, request, url_for
from flask_restful import Api

from engine.resources.container import ContainerResource
from engine.resources.deploy import DeployResource
from settings import *


app = Flask(__name__)
app.config.from_object(__name__)

api = Api(app)


api.add_resource(DeployResource, '/deploy/new',)
api.add_resource(ContainerResource, '/container/all',)