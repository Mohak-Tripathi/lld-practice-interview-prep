class ParkingLotError(Exception):
    """Base for everything this domain raises."""  


class NoSpotAvailable(ParkingLotError):
    pass 

class SpotNotAvailable(ParkingLotError):
    pass


class SpotNotOccupied(ParkingLotError):
    pass

class UnknownTicket(ParkingLotError): 
    pass 


class TicketAlreadyUsed(ParkingLotError):
    pass

class InvalidExitTime(ParkingLotError):
    pass