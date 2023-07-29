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
        cart = self.get_user_cart(user_id)
        if not cart:
            raise Exception(f"User {user_id} not found in cart list")
        
        cart.add(course)
    
    def delete_user(self, user_id: int):
        for index, cart in enumerate(self.user_carts):
            if user_id == cart['user_id']:
                self.user_carts.pop(index)
                return

        raise Exception(f"User {user_id} not found in cart list")
    
    def delete_course(self, user_id: int, course: Course):
        cart = self.get_user_cart(user_id)
        if not cart:
            raise Exception(f"User {user_id} not found in cart list")
        
        cart.remove(course)
    
    def get_user_cart(self, user_id: int) -> Cart:
        for cart in self.user_carts:
            if user_id == cart['user_id']:
                return cart['cart']
            
        return None
