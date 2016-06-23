# encoding: utf-8
from sqlalchemy import Column, Integer, ForeignKey

from rocket.settings import Model


class SpacebusHasContainer(Model):

    """
    """
    __tablename__ = 'spacebus_has_container'
    spacebus_id = Column(Integer, ForeignKey('spacebus.id'), primary_key=True)
    container_id = Column(Integer, ForeignKey('container.id'), primary_key=True)
