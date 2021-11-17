
class Elevator:
    """
    Elevator Class: Receives data and builds an elevator object.
    We built getters and seters even though it is in Python and it is possible to work even without them, because we wanted a clean and tidy job with unequivocal commands and names.
    """

    def __str__(self) -> str:
        ans = f"id: {self.get_id()}"
        ans += f"\t\tspeed: {self.get_speed()}"
        ans += f"\t\tminFloor: {self.get_minFloor()}"
        ans += f"\t\tmaxFloor: {self.get_maxFloor()}"
        ans += f"\ncloseTime: {self.get_closeTime()}"
        ans += f"\t\topenTime: {self.get_openTime()}"
        ans += f"\t\tstartTime: {self.get_startTime()}"
        ans += f"\t\tstopTime: {self.get_stopTime()}"
        return ans

    def __init__(self, id:str=None, speed:float=None, minFloor:int=None, maxFloor:int=None,
                 closeTime:float=None, openTime:float=None,  startTime:float=None,
                 stopTime: float = None):
        self._id = id
        self._speed = speed
        self._minFloor = minFloor
        self._maxFloor = maxFloor
        self._closeTime = closeTime
        self._openTime = openTime
        self._startTime = startTime
        self._stopTime = stopTime

    #Geters:
    def get_id(self) -> int:
        return self._id
    def get_speed(self) -> float:
        return self._speed
    def get_minFloor(self) -> int:
        return self._minFloor
    def get_maxFloor(self) -> int:
        return self._maxFloor
    def get_closeTime(self) -> float:
        return self._closeTime
    def get_openTime(self) -> float:
        return self._openTime
    def get_startTime(self) -> float:
        return self._startTime
    def get_stopTime(self) -> float:
        return self._stopTime
    #Seters:
    def set_id(self, id:int=None) -> None:
        self._id = id
    def set_speed(self, speed:float=None) -> None:
        self._speed = speed
    def set_minFloor(self, minFloor:int=None) -> None:
        self._minFloor = minFloor
    def set_maxFloor(self, maxFloor:int=None) -> None:
        self._maxFloor = maxFloor
    def set_closeTime(self, closeTime:float=None) -> None:
        self._closeTime = closeTime
    def set_openTime(self, openTime:float=None) -> None:
        self._openTime = openTime
    def set_startTime(self, startTime:float=None) -> None:
        self._startTime = startTime
    def set_stopTime(self, stopTime: float = None) -> None:
        self._stopTime = stopTime

