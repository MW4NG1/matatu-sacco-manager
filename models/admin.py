from models.user import User

class Admin(User):
    def __init__(self, user_id: str, name: str, phone_number: str, permissions: list = None):
        super().__init__(user_id, name, phone_number, role="admin")
        self.permissions = permissions or ["manage_users", "manage_routes", "manage_matatus"]

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["permissions"] = self.permissions
        return data

    def __str__(self) -> str:
        return f"Admin({self.name}, Permissions: {len(self.permissions)})"

    