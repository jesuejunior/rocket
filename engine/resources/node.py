# encoding: utf-8
from IPy import IP
from alchemytools.context import managed
from flask import request, jsonify, make_response
from flask_restful import Resource
from sqlalchemy import exists

from rocket.settings import Session
from engine.models.node import Node
from rocket import api_version, api
from toolbox.flask_headers import add_headers

#TODO: Remove queries from view/endpoint
@api.resource('/{0}/nodes'.format(api_version), '/{0}/nodes/<int:id>'.format(api_version))
class NodeResource(Resource):
	@add_headers({'ok': True})
	def get(self, id=None):
		# TODO: Move to queries to model methods
		with managed(Session) as session:
			if id:
				node = session.query(Node).get(id)
				if node:
					node = node.serialize
				response = jsonify(data=node)
			else:
				nodes = session.query(Node).all()
				response = jsonify(data=[node.serialize for node in nodes])
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
					'errorCode': 'node.invalid_field',
					'message': str(ex)
				}
				return make_response(jsonify(data), 400)
			if session.query(exists().where(Node.ip == ip)).scalar():
				data = {
					'errorCode': 'node.exists',
					'message': 'Node already created with ip: {0}'.format(ip)
				}
				return make_response(jsonify(data), 400)
			node = Node(**data)
			session.add(node)
		return make_response(jsonify(), 201)

	def put(self, id):
		# TODO: Implement validations
		data = request.get_json(force=True)
		with managed(Session) as session:
			node = session.query(Node).filter_by(id=id).update(data)
		return make_response(jsonify(data=node), 200)

	def delete(self, id):
		with managed(Session) as session:
			removed = session.query(Node).filter_by(id=id).delete()
		if removed:
			return make_response(jsonify(), 204)
		else:
			data = {
				'errorCode': 'node.not_found',
				'message': 'Node not found'
			}
			return make_response(jsonify(data), 400)
