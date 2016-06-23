# encoding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy_utils import JSONType

from rocket.settings import Model


class Container(Model):

    """
    """
    __tablename__ = 'container'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(40))
    config = Column(JSONType)
