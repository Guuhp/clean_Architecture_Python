from src.infra.database.tests.users_repository import UsersRepositorySpy
from .user_finder import UserFinder


def test_find():
    first_name = 'meunome'
    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    response = user_finder.find(first_name)

    assert repo.select_users_attributes["first_name"] == first_name
    
    assert response["type"] == "Users"
    assert response["count"] == len(response["attributes"])
    assert response["attributes"] != []

def test_find_error_in_invalid_name():
    first_name = 'meuNome123'
    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(first_name)
        assert False
    except Exception as exception:
        assert str(exception) == "Name invalid for the search!"

def test_find_error_in_to_long_name():
    first_name = 'aossisisisisisisisisisisi'
    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(first_name)
        assert False
    except Exception as exception:
        assert str(exception) == "Very big name for the search"

def test_find_error_user_not_found():
    class UserRepositoryError(UsersRepositorySpy):
        def select_user(self, first_name:str):
            return []
    
    first_name = 'meuNome'

    repo = UserRepositoryError()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(first_name)
        assert False
    except Exception as exception:
        assert str(exception) == "User not found"
