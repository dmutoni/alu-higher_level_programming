#!/usr/bin/python3
'''Defines ORM mapping for the city table
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class City(Base):
    '''Definition of city table mapping
    '''
    __tablename__ = "cities"

    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
