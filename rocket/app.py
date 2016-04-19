# encoding: utf-8
import os
from flask import Flask, request, url_for
from flask_restful import Resource, Api

from engine.resources import HelloWorld
from settings import *


app = Flask(__name__)
app.config.from_object(__name__)

api = Api(app)


api.add_resource(HelloWorld, '/')