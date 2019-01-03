from .views.user import User, Users


def includeme(config):
    include_users(config)


def include_users(config):
    include_user(config)
    config.add_route('users', '/api/v1/user')
    config.add_view(Users, attr='get', request_method='GET')
    config.add_view(Users, attr='post', request_method='POST')


def include_user(config):
    config.add_route('user', '/api/v1/user/{ID}')
    config.add_view(User, attr='get', request_method='GET')
    config.add_view(User, attr='put', request_method='PUT')
    config.add_view(User, attr='delete', request_method='DELETE')
