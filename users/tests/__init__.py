from django.test import TestCase
from projects.mongo import get_db, get_connection


class BaseTests(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        print(get_db().name)
        get_connection().drop_database(get_db().name)
