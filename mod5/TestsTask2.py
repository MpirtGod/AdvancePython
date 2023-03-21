import unittest
from mod5.task2 import app

class TestWtform(unittest.TestCase):
    def setUp(self):
        app.config['DEBUG'] = False
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        self.base_url = 'https://localhost/run_code'

    def test_if_ends_by_timeout(self):
        response = self.app.post(self.base_url, data={"code": "import time\nprint(12)\ntime.sleep(5)", "timeout": 3})
        self.assertTrue('Process was killed by timeout' in response.text)

    def test_if_returns_output(self):
        response = self.app.post(self.base_url, data={"code": "import time\nprint(12)\ntime.sleep(5)", "timeout": 3})
        self.assertTrue('12' in response.text)

    def test_no_code_error(self):
        response = self.app.post(self.base_url, data={"timeout": 3})
        self.assertTrue(response.status_code == 400)

    def test_no_timeout_error(self):
        response = self.app.post(self.base_url, data={"code": "import time\nprint(12)\ntime.sleep(50)"})
        self.assertTrue('10' in response.text)

    def test_bigger_than_expected_timeout_error(self):
        response = self.app.post(self.base_url, data={"code": "import time\nprint(12)\ntime.sleep(5)", "timeout": 35})
        self.assertTrue(response.status_code == 400)

    def test_unsafe_code(self):
        response = self.app.post(self.base_url, data={'code': 'from subprocess import run\nrun([\'./kill_the_system.sh\'])', "timeout": 3})
        self.assertTrue('Resource temporarily unavailable' in response.text)