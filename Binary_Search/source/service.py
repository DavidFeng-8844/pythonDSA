import pytest

database = {
    1: "david",
    2: "mary",
    3: "john"
}


def get_user_from_db(user_id):
    return database[user_id]
