from .users_repository import UsersRepository


def test_insert_user():
    mocked_first_name = "first"
    mocked_last_name = "last"
    mocked_age = 22

    user_repository = UsersRepository()
    user_repository.insert(mocked_first_name, mocked_last_name, mocked_age)
