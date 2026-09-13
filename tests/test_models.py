import pytest
from models.route import Route
from models.user import User
from models.matatu import Matatu

def test_route_creation_and_to_dict():
    route = Route("R1", "CBD", "Westlands", 100)
    assert route.route_id == "R1"
    assert route.source == "CBD"
    assert route.destination == "Westlands"
    assert route.fare == 100.0

    data = route.to_dict()
    assert data["route_id"] == "R1"
    assert data["fare"] == 100.0

    
    
    