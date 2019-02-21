from __future__ import absolute_import

from .mongo import create as create_mongo_engine
from .providers import create as inject_clear_and_configure

inject_clear_and_configure()
create_mongo_engine()
