#!/usr/bin/python
import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey


class language():
    """I create the fantasy class which tells you about a the original work of the language you want to know"""
    __tablename__ = 'languages'
    Lan_name = Column(String(20), primary_key=True, nullable=False)
    Description = Column(String(100), nullable=False)
    fan = Column(String(50), ForeignKey('Fan_name'), nullable=False)


def __init__(self, *args, **kwargs):
    """initializes language of the middle earth"""
