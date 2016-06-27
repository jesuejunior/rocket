# encoding: utf-8
from flask import Flask
from flask_restful import Api

from engine.resources.node import NodeResource

app = Flask(__name__)
app.config.from_object('settings')

api = Api(app)

api.add_resource(NodeResource,'/nodes', '/nodes/<int:id>')
