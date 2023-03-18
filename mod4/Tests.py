import unittest
from mod4.app import app

class TestWtform(unittest.TestCase):
    def setUp(self):
        app.config['DEBUG'] = False
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        self.base_url = 'https://localhost/registration'

    def test_success(self):
        response = self.app.post(self.base_url, data={"email": "admin@mail.com", "phone": 9028765432, "name": "Sasha", "address": "Have", "index": 344523})
        assert (response.status_code == 200)

    def test_email_error(self):
        response = self.app.post(self.base_url, data={"email": "adminmail.com", "phone": 9028765432, "name": "Sasha", "address": "Have", "index": 344523})
        assert (response.status_code == 400)

    def test_numeric_email_error(self):
        response = self.app.post(self.base_url, data={"email": 123, "phone": 9028765432, "name": "Sasha", "address": "Have", "index": 344523})
        assert (response.status_code == 400)

    def test_bigger_phone_error(self):
        response = self.app.post(self.base_url, data={"email": "admin@mail.com", "phone": 89028765432, "name": "Sasha", "address": "Have", "index": 344523})
        assert (response.status_code == 400)

    def test_string_phone_error(self):
        response = self.app.post(self.base_url, data={"email": "admin@mail.com", "phone": '9028765432', "name": "Sasha", "address": "Have", "index": 344523})
        assert (response.status_code == 400)

    def test_numeric_name_error(self):
        response = self.app.post(self.base_url, data={"email": "admin@mail.com", "phone": 9028765432, "name": 123, "address": "Have", "index": 'Russia'})
        assert (response.status_code == 400)

    def test_numeric_numeric_error(self):
        response = self.app.post(self.base_url, data={"email": "admin@mail.com", "phone": 9028765432, "name": "Sasha", "address": 123, "index": 'Russia'})
        assert (response.status_code == 400)

    def test_string_index_error(self):
        response = self.app.post(self.base_url, data={"email": "admin@mail.com", "phone": 9028765432, "name": "Sasha", "address": "Have", "index": 'Russia'})
        assert (response.status_code == 400)

    def test_no_email_error(self):
        response = self.app.post(self.base_url, data={"phone": 9028765432, "name": "Sasha", "address": "Have", "index": 344523})
        assert (response.status_code == 400)

    def test_no_phone_error(self):
        response = self.app.post(self.base_url, data={"email": "admin@mail.com", "name": "Sasha", "address": "Have", "index": 344523})
        assert (response.status_code == 400)

    def test_no_name_error(self):
        response = self.app.post(self.base_url, data={"email": "admin@mail.com", "phone": 9028765432, "address": "Have", "index": 344523})
        assert (response.status_code == 400)

    def test_no_address_error(self):
        response = self.app.post(self.base_url, data={"email": "admin@mail.com", "phone": 9028765432, "name": "Sasha", "index": 344523})
        assert (response.status_code == 400)

    def test_no_index_error(self):
        response = self.app.post(self.base_url, data={"email": "admin@mail.com", "phone": 9028765432, "name": "Sasha", "address": "Have"})
        assert (response.status_code == 400)