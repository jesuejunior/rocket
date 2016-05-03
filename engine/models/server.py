# encoding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy_utils import IPAddressType, PasswordType

from engine.models import Model


class Server(Model):

	"""
	"""
	__tablename__ = 'server'

	id = Column(Integer, primary_key=True)
	name = Column(String(155), nullable=False)
	so = Column(String(40))
	provider = Column(String(40))
	ip = Column(IPAddressType, unique=True)
	username = Column(String(155), nullable=False)
	password = Column(PasswordType(
		schemes=[
			'pbkdf2_sha512',
			'md5_crypt'
		],
		deprecated=['md5_crypt']
	))
	private_key = Column()