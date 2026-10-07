from dataclasses import dataclass

from .enums import VehicleType 

from .exceptions import SpotNotAvailable, SpotNotOccupied, InvalidExitTime, TicketAlreadyUsed, NoSpotAvailable, UnknownTicket

from math import ceil 
from datetime import datetime 
import uuid

@dataclass(frozen=True)
class Vehicle:
    plate:str 
    type:VehicleType


class ParkingSpot:

    def __init__(self, spot_id:str, vehicle_type: VehicleType):
        self._spot_id = spot_id
        self._vehicle_type = vehicle_type
        self._is_occupied = False

    def can_fit(self, vehicle_type: VehicleType)-> bool:
        return vehicle_type == self._vehicle_type and not self._is_occupied


    def occupy(self, vehicle_type: VehicleType) -> None:
        if not self.can_fit(vehicle_type):
            raise SpotNotAvailable()
        self._is_occupied = True 
        

    def release(self)-> None:
        if not self._is_occupied:
            raise SpotNotOccupied()
        self._is_occupied = False
        

    @property 
    def id(self):
        return self._spot_id

    @property 
    def type(self):
        return self._vehicle_type


class Ticket:

    def __init__(self, ticket_id:str, spot, vehicle, entry_time):
        self._ticket_id = ticket_id
        self._spot = spot
        self._vehicle = vehicle
        self._entry_time = entry_time 
        self._is_used = False 


    def  close(self,exit_time, hourly_rate:int):
        if self._is_used:
            raise TicketAlreadyUsed()
        if exit_time < self._entry_time:
            raise InvalidExitTime()
        seconds = (exit_time - self._entry_time).total_seconds()
        hours = ceil(seconds/ 3600)
        fee = hours * hourly_rate
        self._is_used = True
        return fee

    @property 
    def spot(self):
        return self._spot 

    @property
    def id(self):
        return self._ticket_id


class ParkingLot:
    def __init__(self, spots:list, hourly_rate:int):
        self._spots = spots 
        self._active_tickets = {}
        self._hourly_rate = hourly_rate


    def park(self, vehicle, entry_time) -> Ticket:
        spot = self._find_available(vehicle.type)

        if spot is None:
            raise NoSpotAvailable()
        spot.occupy(vehicle.type)
        ticket = Ticket(str(uuid.uuid4()),spot, vehicle, entry_time)
        self._active_tickets[ticket.id] = ticket
        return ticket


    def exit(self,ticket_id, exit_time) -> float: 
        ticket = self._active_tickets.get(ticket_id)

        if ticket is None:
            raise UnknownTicket()

        fee = ticket.close(exit_time, self._hourly_rate) # tell the ticket
        ticket.spot.release()                            # tell the spot
        del self._active_tickets[ticket_id]              # clean up
        return fee    
    

    def available_spots(self, vehicle_type) -> int:
        count = 0
        for spot in self._spots:
            if spot.can_fit(vehicle_type):
                count += 1
        return count

    def _find_available(self, vehicle_type) -> ParkingSpot | None:

        for spot in self._spots:
            if spot.can_fit(vehicle_type):
                return spot 

        return None


    


         

     