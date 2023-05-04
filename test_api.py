import os
import json
import unittest
from api import app
from flask_testing import TestCase

class TestApp(TestCase):
    def create_app(self):
        os.environ['FLASK_ENV'] = 'development'
        app.config['TESTING'] = True
        return app

class TestSampleTest(TestApp):
    def test_hello(self):
        response = self.client.get('/hello', content_type='application/json')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
