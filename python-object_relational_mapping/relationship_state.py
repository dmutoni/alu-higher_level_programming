#!/usr/bin/python3
'''Defines an ORM for State class
'''
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from relationship_city import City, Base


class State(Base):
    '''Definition of mapping for states table inherits from Base
    '''
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
