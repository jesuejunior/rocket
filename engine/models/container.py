# encoding: utf-8
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import JSONType

from rocket.settings import Model


class Container(Model):

    """
    """
    __tablename__ = 'container'

    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    config = Column(JSONType)
    spacebus_id = Column(Integer, ForeignKey('spacebus.id'))
    spacebus = relationship("Spacebus", back_populates="spacebus")
