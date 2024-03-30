from src.infra.database.repositories.users_repository import UsersRepository
from .user_finder import UserFinder


def test_find():
    repo = UsersRepository()
    user_finder = UserFinder(repo)
