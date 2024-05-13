#!/usr/bin/python

import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String


class fantasy():
    """I create the fantasy class which tells you about a the original work of the language you want to know"""
    __tablename__ = 'fantasy'
    Fan_name = Column(String(50), primary_key=True, nullable=False)
    Fan_synopsis = Column(String(200), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes fantasy world"""
