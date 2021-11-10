from Elevator import Elevator

class Building:

    def __init__(self, _minFloor: int = None, _maxFloor: int = None, elevDict:Elevator=None):
        self._minFloor = _minFloor
        self._maxFloor = _maxFloor
        self._elevDict = {}


    def get_minFloor(self):
        return self._minFloor

    def get_maxFloor(self):
        return self._maxFloor

    def get_elevDict(self) -> dict:
        return self._elevDict

    def __add__(self, elev:Elevator):
        i = elev.get_id()
        self._elevDict[str(i)] = elev
        return self

    def __str__(self) -> str:
        ans = "--------------------------------------------------------------------------------------\n"
        ans += f"minFloor: {self._minFloor}\tmaxFloor: {self._maxFloor}"
        dictionary_items = self.get_elevDict().items()
        for elev in dictionary_items:
            ans += "\n\n"+str(elev[1])
        ans += "\n--------------------------------------------------------------------------------------"
        return ans
