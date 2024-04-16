from typing import List
from src.domain.models.users import Users


class UsersRepositorySpy():

    def __init__(self) -> None:
        self.insert_users_attributes = {}
        self.select_users_attributes = {}

    def insert(self, first_name: str, last_name: str, age: int) -> None:
        self.insert_users_attributes['first_name'] = first_name
        self.insert_users_attributes['last_name'] = last_name
        self.insert_users_attributes['age'] = age
        return

    def select_user(self, first_name: str) -> List[Users]:
        self.select_users_attributes['first_name'] = first_name
        return[
            Users(23, first_name,'last','43'),
            Users(23, first_name,'last_2','43')
        ]
        
