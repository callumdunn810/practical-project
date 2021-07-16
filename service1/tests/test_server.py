from application import app,db
from flask import url_for
from flask_testing import TestCase
import requests_mock
from unittest.mock import patch
from application.models import Character



# class TestBase(TestCase):
#     def create_app(self):

 
#         app.config.update(SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:Grg170dx@34.105.231.190:3306/generatedb',
#                 SECRET_KEY='TEST_SECRET_KEY',
#                 DEBUG=True,
#                 WTF_CSRF_ENABLED=False
#                 )
#         return app

#     def setUp(self):
#         """
#         Will be called before every test
#         """
#         db.create_all()

#         skill1 = Character(skill="Necromancer")

#         db.session.add(skill1)

#         db.session.commit()

#     def tearDown(self):
#         """
#         Will be called after every test
#         """

#         db.session.remove()
#         db.drop_all()



############################################################################################################


class TestBase(TestCase):
    def create_app(self):
        return app 
        
class TestViews(TestBase):
    def test_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'ELDERSCROLLS ONLINE CHARACTER GENERATOR', response.data)

# class TestAdd(TestBase):
#     def test_add_post(self):
#         response = self.client.post(
#             url_for('gen'),
#             data = dict(race="Dark Elf"),
#             follow_redirects=True
#         )
#         self.assertIn(b'Dark Elf',response.data)



class TestBase(TestCase):
    def create_app(self):
        return app


class TestHome(TestBase):
    def test_home(self):
        with requests_mock.Mocker() as mocker:
            mocker.get('http://service2-skill:5000/get_skill', text='Nightblade')
            mocker.get('http://service3-alliance:5000/get_alliance', text='Ebonheart Pact')
            mocker.post('http://service4-race:5000/get_race', text='Dark Elf')
            response = self.client.get(url_for('gen'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Class: Nightblade',response.data)
            self.assertIn(b'Alliance: Ebonheart Pact',response.data)
            self.assertIn(b'Race: Dark Elf',response.data)


####################################################################################
