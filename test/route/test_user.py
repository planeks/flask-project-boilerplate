import json
import unittest

from src.server import server
from src.model import db
from src.model import User


class TestUser(unittest.TestCase):

    def setUp(self):
        server.config['TESTING'] = True
        self.client = server.test_client()

        db.create_all()

        self.user = User('joe@example.fr', 'super-secret-password')
        db.session.add(self.user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_user(self):

        response = self.client.get(
            '/user/%d' % self.user.id,
        )
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['email'], 'joe@example.fr')

if __name__ == '__main__':
    unittest.main()
