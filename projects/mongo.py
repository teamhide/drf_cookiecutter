from __future__ import absolute_import

import mongoengine
from pymongo import MongoClient
from pymongo.database import Database

from projects.settings import DATABASES


def create():
    mongoengine.connect(
        db=DATABASES.get('mongo').get('NAME'),
        host=DATABASES.get('mongo').get('CONNECTION'),
    )


def get_db() -> Database:
    return mongoengine.connection.get_db()


def get_connection() -> MongoClient:
    return mongoengine.connection.get_connection()
