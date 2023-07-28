from datetime import datetime
from typing import Dict, List, Any
from tgbot.models.Cart import Cart
from tgbot.models.Course import Course


class CartController:
    def __init__(self):
        self.user_carts: List[Dict[str, Any]] = []

    def add_user(self, user_id: int, created: datetime):
        self.user_carts.append({
            "user_id": user_id,
            "cart": Cart(user_id, created=created, last_updated=created)
        })

    def add_course(self, user_id: int, course: Course) -> bool:
        for cart in self.user_carts:
            if user_id == cart['user_id']:
                cart['cart'].add(course)
                return True

        raise Exception(f"User {user_id} not found in cart list")

    def delete_course(self, user_id: int, course: Course):
        for cart in self.user_carts:
            if user_id == cart['user_id']:
                cart['cart'].remove(course)
                return

        raise Exception(f"User {user_id} not found in cart list")
