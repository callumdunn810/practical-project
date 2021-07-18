from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

from application import app



class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_skill(self):
        with patch('random.choice') as r:
            r.return_value = 'Necromancer'
            response = self.client.get(url_for('get_skill'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Necromancer',response.data)
