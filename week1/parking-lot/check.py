from datetime import datetime
from src.models import Ticket, Vehicle, ParkingSpot
from src.enums import VehicleType

s = ParkingSpot("A1", VehicleType.CAR)
t = Ticket("T1", s, Vehicle("KA01", VehicleType.CAR), datetime(2026,1,1,10,0))
print(t.close(datetime(2026,1,1,12,30), 20))   # expect 60