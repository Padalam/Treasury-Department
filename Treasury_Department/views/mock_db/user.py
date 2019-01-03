from .models.user import User
from dataclasses import asdict

users = [
    User(ID=1, nickname='lol1'),
    User(ID=2, nickname='lol2'),
    User(ID=3, nickname='lol3')
]


def get_users() -> [User]:
    return users


def post_users(user: User) -> User:
    return user


def get_user(ID: int) -> User:
    for value in users:
        if value.ID == ID:
            return value


def put_user(ID: int, new_user: User) -> User:
    return new_user


def del_user(ID: int) -> User:
    for value in users:
        if value.ID == ID:
            return value
