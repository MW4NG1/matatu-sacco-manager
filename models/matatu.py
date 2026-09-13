class Matatu:
    def __init__(self, registration_number: str, capacity: int, driver_id: str = None, route_id: str = None):
        self.registration_number = registration_number
        self.capacity = int(capacity)
        self.driver_id = driver_id
        self.route_id = route_id

    def assign_driver(self, driver_id: str):
        self.driver_id = driver_id

    def assign_route(self, route_id: str):
        self.route_id = route_id

    def to_dict(self) -> dict:
        return {
            "registration_number": self.registration_number,
            "capacity": self.capacity,
            "driver_id": self.driver_id,
            "route_id": self.route_id
        }

    def __str__(self) -> str:
        return f"Matatu({self.registration_number}, Capacity: {self.capacity})"
    