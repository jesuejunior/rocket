# encoding: utf-8
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import validates
from sqlalchemy_utils import PasswordType

from rocket.settings import Model


class User(Model):
	"""
	"""
	__tablename__ = 'user'

	id = Column(Integer, primary=True, autoincrement=True)
	first_name = Column(String)
	last_name = Column(String)
	email = Column(String, unique=True)
	is_active = Column(Boolean)
	password = Column(PasswordType(
        schemes=[
            'pbkdf2_sha512',
            'md5_crypt'
        ],
        deprecated=['md5_crypt']
    ),
	unique=False,
	nullable=False
	)

	@validates('email')
	def validate_email(self, key, address):
		assert '@' in address
		return address
