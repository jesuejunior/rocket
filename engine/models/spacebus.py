# encoding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from engine.models import Model


class Spacebus(Model):

    """
    """
    __tablename__ = 'spacebus'

    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    container = relationship("Ccontainer", secundary='spacebus_has_container', backref="spacebuses")
