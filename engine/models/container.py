# encoding: utf-8
from sqlalchemy import Column, Integer, String

from engine.models import Model


class Container(Model):

    """
    """
    __tablename__ = 'spacebus'

    id = Column(Integer, primary_key=True)
    name = Column(String(40))
