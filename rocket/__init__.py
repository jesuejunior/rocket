# encoding: utf-8
from flask import Flask
from flask_restful import Api

from engine.resources.node import node, NodeResource
from rocket.settings import API_VERSION

app = Flask(__name__)
app.config.from_object('settings')

app.register_blueprint(node)

api = Api(app)

api.add_resource(NodeResource,'/{0}/nodes'.format(API_VERSION), '/{0}/nodes/<int:id>'.format(API_VERSION))
