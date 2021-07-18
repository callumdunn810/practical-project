from flask import url_for
from flask_testing import TestCase
import requests_mock
from unittest.mock import patch

from application import app



class TestBase(TestCase):
    def create_app(self):
        return app


class TestHome(TestBase):
    def test_alliance(self):
        with patch('random.choice') as r:
            r.return_value = 'Daggerfall Covenant'
            response = self.client.get(url_for('get_alliance'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Daggerfall Covenant', response.data)
