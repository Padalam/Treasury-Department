import unittest

from pyramid import testing


class UsersViewTests(unittest.TestCase):
    def setUp(self):
        from Treasury_Department import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)
        self.test_body = {'ID': 1, 'nickname': 'lol1'}

    # Users
    def test_post_users(self):
        res = self.testapp.post_json(
            '/api/v1/user', self.test_body)
        self.assertTrue({'user': self.test_body} == res.json)

    def test_not_post_users_none_id(self):
        body = self.test_body
        del body['ID']
        with self.assertRaises(Exception):
            self.testapp.post_json('/api/v1/user', body)

    def test_not_post_users_none_nickname(self):
        body = self.test_body
        del body['nickname']
        with self.assertRaises(Exception):
            self.testapp.post_json('/api/v1/user', body)

    def test_get_users(self):
        res = self.testapp.get('/api/v1/user')
        self.assertTrue('users' in res.json)

    # User
    def test_get_user(self):
        res = self.testapp.get(f"/api/v1/user/{self.test_body['ID']}")
        self.assertTrue({'user': self.test_body} == res.json)

    def test_put_user(self):
        body = dict(self.test_body)
        del body['ID']
        body['nickname'] = 'lol4'
        print(body)
        res = self.testapp.put_json(
            f"/api/v1/user/{self.test_body['ID']}", body)
        print(res.json)
        self.assertTrue('lol4' == res.json['user']['nickname'])

    def test_delete_user(self):
        res = self.testapp.delete(f"/api/v1/user/{self.test_body['ID']}")
        self.assertTrue({'user': self.test_body} == res.json)
