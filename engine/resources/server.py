# encoding: utf-8
# encoding: utf-8
from alchemytools.context import managed
from flask import request
from flask_restful import Resource

from engine.models import Session
from engine.models.server import Server


class ServerResource(Resource):
	def get(self, id):
		with managed(Session) as session:
			server = session.query(Server).get(id)

		return {'data': server}

	def post(self):
		data = request.get_json(force=True)
		with managed(Session) as session:
			server = Server()
			session.add(server)
		print(data)
		return True

