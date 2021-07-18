from flask import url_for
from flask_testing import TestCase
import requests_mock
from unittest.mock import patch

from application import app



class TestBase(TestCase):
    def create_app(self):
        return app


class TestHome(TestBase):
    def test_race(self):
        response = self.client.post(url_for('get_race'), data='Aldmeri Dominion')
        self.assertEqual(response.data.decode("utf-8"),'High Elf')
