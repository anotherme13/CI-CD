import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        # Set up a test client before each test
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_content(self):
        response = self.app.get('/')
        self.assertIn(b"THIS IS A TEST PAGE", response.data)

    def test_health_endpoint(self):
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"healthy", response.data)

if __name__ == '__main__':
    unittest.main()
