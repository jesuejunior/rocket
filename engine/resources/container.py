# encoding: utf-8

from flask_restful import Resource
from docker import Client

from rocket.settings import api


@api.resource('/containers')
class ContainerResource(Resource):

	def get(self, id):
		cli = Client(base_url='tcp://192.168.1.105:2375')
		c = None
		return {'container': c}
