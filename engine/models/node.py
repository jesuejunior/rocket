# encoding: utf-8
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy_utils import IPAddressType, EncryptedType

from rocket.settings import Model, SECRET_KEY


class Node(Model):

    """
    """
    __tablename__ = 'node'

    id = Column(Integer, primary_key=True)
    name = Column(String(155), nullable=False)
    so = Column(String(40))
    provider = Column(String(40))
    ip = Column(IPAddressType, unique=True)
    fqdn = Column(String(50), nullable=True)
    username = Column(String(155), nullable=False)
    password = Column(EncryptedType(String, SECRET_KEY), nullable=True)
    private_key = Column(EncryptedType(String, SECRET_KEY), nullable=True)
    ready = Column(Boolean, default=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'so': self.so,
            'provider': self.provider,
            'ip': str(self.ip),
            'fqdn': self.fqdn,
            'username': self.username,
            'password': self.password,
            'private_key': self.private_key
        }

    def add(self):

        return True
