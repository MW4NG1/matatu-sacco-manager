class User:
    def __init__(self, user_id: str, name: str, phone_number: str, role: str = "passenger"):
        self.user_id = user_id
        self.name = name
        self.phone_number = phone_number
        self.role = role

    def to_dict(self) -> dict:
        return {
            "user_id": self.user_id,
            "name": self.name,
            "phone_number": self.phone_number,
            "role": self.role
        }

    def __str__(self) -> str:
        return f"User({self.name}, Role: {self.role})"