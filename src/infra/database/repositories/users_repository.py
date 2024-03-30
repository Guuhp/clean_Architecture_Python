from src.infra.database.settings.connection import DBConnectionHandler
from src.infra.database.entities.users import Users as UserEntity


class UsersRepository:

    @classmethod
    def insert(cls, first_name: str, last_name: str, age: int) -> None:
        with DBConnectionHandler() as database:
            try:
                new_register = UserEntity(
                    first_name=first_name, last_name=last_name, age=age
                )
                database.session.add(new_register)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
