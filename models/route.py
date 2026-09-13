class Route:
    def __init__(self, route_id: str, source: str, destination: str, fare: float):
        self.route_id = route_id
        self.source = source
        self.destination = destination
        self.fare = float(fare)

    def update_fare(self, new_fare: float):
        self.fare = float(new_fare)

    def to_dict(self) -> dict:
        return {
            "route_id": self.route_id,
            "source": self.source,
            "destination": self.destination,
            "fare": self.fare
        }

    def __str__(self) -> str:
        return f"Route({self.source} -> {self.destination}, Fare: {self.fare})"