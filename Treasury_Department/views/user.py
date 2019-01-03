from pyramid.view import view_defaults, view_config
from dataclasses import dataclass, asdict
from .mock_db.models import user as model_user
from .mock_db import user as mock_db_user


@view_defaults(route_name='users', renderer='json')
class Users(object):
    def __init__(self, request):
        """
        Get params only for post User
        """
        self.request = request

    def get(self):
        return {'users': [asdict(x) for x in mock_db_user.get_users()]}

    def post(self):
        if (not 'ID' in self.request.json or
                    not 'nickname' in self.request.json
                ):
            self.request.response.status = 400
            return None
        post_user = model_user.User(
            ID=self.request.json.get('ID') or None, nickname=self.request.json.get('nickname') or None)
        ret_val = mock_db_user.post_users(post_user)
        if ret_val:
            return {'user': asdict(ret_val)}
        else:
            return None


@view_defaults(route_name='user', renderer='json')
class User(object):
    def __init__(self, request):
        self.request = request

    def get(self):
        ret_val = mock_db_user.get_user(int(self.request.matchdict['ID']))
        if ret_val:
            return {'user': asdict(ret_val)}
        else:
            self.request.response.status = 400
            return None

    def put(self):
        if (
            not 'nickname' in self.request.json
        ):
            self.request.response.status = 400
            return None
        put_user = model_user.User(
            ID=int(self.request.matchdict['ID']) or None, nickname=self.request.json.get('nickname') or None)
        ret_val = mock_db_user.put_user(
            int(self.request.matchdict['ID']), put_user)
        print(f"ret_val_status: {ret_val}")
        if (ret_val):
            return {'user': asdict(ret_val)}
        else:
            return None

    def delete(self):
        ret_val = mock_db_user.del_user(int(self.request.matchdict['ID']))
        if ret_val:
            return {'user': asdict(ret_val)}
        else:
            self.request.response.status = 400
            return None
