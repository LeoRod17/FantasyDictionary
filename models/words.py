#!/usr/bin/python
import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey


class language():
    """I create the class to divide the words in what they mean in our language and what they look like
    because not all the languages have the same simbols in they world"""
    __tablename__ = 'words'
    word_name = Column(String(20), primary_key=True, nullable=False)
    meaning = Column(String(100), nullable=False)
    usage = Column(String(50))
    img = Column(String(50), nullable=False)
    lang = Column(String(50), ForeignKey('Lan_name'), nullable=False)


def __init__(self, *args, **kwargs):
    """initializes language of the middle earth"""
