import json
import unittest

from flask import current_app

from app import create_app
from model import db


class TestAPP(unittest.TestCase):
    def login(self, username):
        params = {'username': username}
        return self.client.post('/login', data=params, follow_redirects=True)

    def register(self, username):
        params = {'username': username}
        return self.client.post('/register', data=params, follow_redirects=True)

    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_config(self):
        self.assertEqual(self.app.config['TESTING'], True)
        self.assertIsNotNone(self.app.config['SQLALCHEMY_DATABASE_URI'])

    def test_index(self):
        ret = self.client.get('/')
        self.assertEqual(b'Hello world!', ret.data)

    def test_register(self):
        ret = self.register('bar')
        self.assertEqual(json.loads(ret.data)['success'], True)
    
    def test_login(self):
        self.register('foo')
        ret = self.login('foo')
        return self.assertEqual(json.loads(ret.data)['username'], 'foo')

    def test_noRegisterLogin(self):
        ret = self.login('foo')
        return self.assertEqual(json.loads(ret.data)['success'], False)

    def test_login_get(self):
        ret = self.client.get('/login', follow_redirects=True)
        self.assertIn(b'Method Not Allowed', ret.data)

# class TestAPPOrder(unittest.TestSuite):
#     def test_all(self):
#         tests = [TestAPP('test_register'), TestAPP('test_login'), TestAPP('test_noRegisterLogin'), TestAPP('test_login_get')]
#         self.addTests(tests)
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
    # suite = unittest.TestSuite()
    # tests = [TestAPP('test_register'), TestAPP('test_login'), TestAPP('test_noRegisterLogin'), TestAPP('test_login_get')]
    # suite.addTests(tests)
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)
