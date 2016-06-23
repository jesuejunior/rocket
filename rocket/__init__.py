# encoding: utf-8
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
app.config.from_object(__name__)


api = Api(app)

api_version = 'v1'