# encoding: utf-8

from flask import request
from flask_restful import Resource
from docker import Client


class ContainerResource(Resource):

	def get(self):
		cli = Client(base_url='tcp://192.168.1.105:2375')
		c = cli.containers()
		return {'containers': c}