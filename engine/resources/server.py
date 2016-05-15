# encoding: utf-8
from alchemytools.context import managed
from flask import request, jsonify, make_response
from flask_restful import Resource
from sqlalchemy import exists
from IPy import IP
from toolbox.flask_headers import add_headers
from engine.models import Session
from engine.models.server import Server


class ServerResource(Resource):
	@add_headers({'ok': True})
	def get(self, id=None):
		# TODO: Move to queries to model methods
		with managed(Session) as session:
			if id:
				server = session.query(Server).get(id)
				if server:
					server = server.serialize
				response = jsonify(data=server)
			else:
				servers = session.query(Server).all()
				response = jsonify(data=[server.serialize for server in servers])
		return make_response(response, 200)

	def post(self):
		# TODO: Move returned error message to constant in another file
		data = request.get_json(force=True)
		with managed(Session) as session:
			ip = data.get('ip')
			try:
				IP(ip)
			except ValueError as ex:
				data = {
					'errorCode': 'server.invalid_field',
					'message': str(ex)
				}
				return make_response(jsonify(data), 400)
			if session.query(exists().where(Server.ip == ip)).scalar():
				data = {
					'errorCode': 'server.exists',
					'message': 'Server already created with ip: {0}'.format(ip)
				}
				return make_response(jsonify(data), 400)
			server = Server(**data)
			session.add(server)
		return make_response(jsonify(), 201)

	def put(self, id):
		# TODO: Implement validations
		data = request.get_json(force=True)
		with managed(Session) as session:
			server = session.query(Server).filter_by(id=id).update(data)
		return make_response(jsonify(data=server), 200)

	def delete(self, id):
		with managed(Session) as session:
			removed = session.query(Server).filter_by(id=id).delete()
		if removed:
			return make_response(jsonify(), 204)
		else:
			data = {
				'errorCode': 'server.not_found',
				'message': 'Server not found'
			}
			return make_response(jsonify(data), 400)
