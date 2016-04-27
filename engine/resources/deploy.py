# encoding: utf-8
from flask import request
from flask_restful import Resource


class DeployResource(Resource):
	def get(self):
		return {'result': True}

	def post(self):
		data = request.get_json(force=True)
		print(data)
		return True

