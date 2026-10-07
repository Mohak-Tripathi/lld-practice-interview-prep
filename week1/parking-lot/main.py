from datetime import datetime 


from src.enums import VehicleType 

from src.models import Vehicle, ParkingSpot, ParkingLot

def main() -> None: 
    #--- build the lot ---
    spots = [
        ParkingSpot("M1", VehicleType.MOTORCYCLE),
        ParkingSpot("C1", VehicleType.CAR),
        ParkingSpot("C2", VehicleType.CAR),
        ParkingSpot("T1", VehicleType.TRUCK),
             ]


    lot = ParkingLot(spots, hourly_rate =20)

    # ---- flow 1: park a car ----
    car = Vehicle("KA01AB1234", VehicleType.CAR)
    entry = datetime(2026, 1, 1, 10, 0)

    print("cars free before parking:", lot.available_spots(VehicleType.CAR))
    ticket = lot.park(car, entry)
    print("issued ticket:", ticket.id, "at spot", ticket.spot.id)
    print("cars free after parking:", lot.available_spots(VehicleType.CAR))

        # ---- flow 2: exit and pay ----
    exit_time = datetime(2026, 1, 1, 12, 30)
    fee = lot.exit(ticket.id, exit_time)
    print("fee for 2.5 hours at rate 20:", fee)
    print("cars free after exit:", lot.available_spots(VehicleType.CAR))


if __name__ == "__main__":
    main()

    