# encoding: utf-8
from flask.ext.restful.fields import Integer, String
from sqlalchemy import Column
from sqlalchemy_utils import IPAddressType, PasswordType

from engine.models import Model


class Server(Model):

    """

    """
    __tablename__ = 'server'

    id = Column(Integer, primary_key=True)
    name = Column(String(155), nullable=False)
    ip = Column(IPAddressType)
    username = Column(String(155), nullable=False)
    password = Column(PasswordType(
        schemes=[
            'pbkdf2_sha512',
            'md5_crypt'
        ],
        deprecated=['md5_crypt']
    ))
    private_key = Column()