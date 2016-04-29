# encoding: utf-8
from flask.ext.restful.fields import Integer, String
from sqlalchemy import Column

from engine.models import Model


class Server(Model):

    """

    """

    __tablename__ = 'server'

    id = Column(Integer, primary_key=True)
    name = Column(String(155), nullable=False)