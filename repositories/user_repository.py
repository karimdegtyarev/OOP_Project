from typing import List, Optional
from models.user import User


class UserRepository:
    def __init__(self):
        self.users = []
        self.next_id = 1

    def get_all(self) -> List[User]:
        return self.users

    def get_by_id(self, user_id: int) -> Optional[User]:
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def create(self, user: User) -> User:
        # Проверка уникальности username
        if any(u.username == user.username for u in self.users):
            raise ValueError("Имя пользователя уже занято")

        # Проверка уникальности email
        if any(u.email == user.email for u in self.users):
            raise ValueError("Email уже используется")

        user.id = self.next_id
        self.next_id += 1
        self.users.append(user)
        return user

    def update(self, user_id: int, user_update: User) -> Optional[User]:
        for i, user in enumerate(self.users):
            if user.id == user_id:
                updated_user = user.copy(update=user_update.dict(exclude_unset=True))
                self.users[i] = updated_user
                return updated_user
        return None

    def delete(self, user_id: int) -> bool:
        for i, user in enumerate(self.users):
            if user.id == user_id:
                del self.users[i]
                return True
        return False