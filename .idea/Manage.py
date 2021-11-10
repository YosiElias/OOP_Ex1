from Building import Building
from Elevator import Elevator
from Calls import Calls
import math


class Manage:

    def __init__(self, b:Building=None):
        self._b = b
        self._elevDict = b.get_elevDict()
        self._callList = {}
        for elev in b.get_elevDict().keys():    #init list for all the elevator
            self._callList[str(b.get_elevDict().get(elev).get_id())] = []
        self._direction = {}

    def get_state(self,  id:str=None, time:float=0.0) -> str:
        """
        :return: "LEVEL"/"UP"/"DOWN"
        """
        elevCalls = self._callList.get(str(id))  # list of Calls
        i = len(elevCalls) - 1
        for call in elevCalls.__reversed__():
            if call.get_time_dst() <= time and i==len(elevCalls)-1: #the last call
                return "LEVEL"
                break
            elif call.get_time_dst() <= time:
                return call.get_dirc()
                break
            elif call.get_time_src() <= time:
                return call.get_dirc()
                break


    def getPos(self, id:str=None, time:float=0.0) -> int:
        """
        :param id: id of elev
        :param time: time to know where th elev is
        :return: where th elev is in time 'time'
        """
        floor = 0 # defulte of elevator before first move
        # if self._direction.get(id) == "UP":
        elevCalls = self._callList.get(str(id)) #list of Calls
        i = len(elevCalls) - 1
        for call in elevCalls.__reversed__():
            if call.get_time_dst() <= time:
                floor = self.posFrom(srcFloor=call.get_dest(), plusTime=(time - call.get_time_dst()), id=id, callNumber=i, isdest=True)
                break
            elif call.get_time_src() <= time:
                floor = self.posFrom(srcFloor=call.get_src(), plusTime=time - call.get_time_src(), id=id, callNumber=i, isdest=False)
                break
        i = i-1
        return floor


    def posFrom(self, srcFloor:int=None, plusTime:float=None, id:str=None, callNumber:int=None, isdest:bool=None) ->float:
        """
        :rtype: float of floor get from srcFloor to time 'plusTime'
        """
        elev = self._elevDict.get(str(id))
        elevCalls = self._callList.get(str(id))
        if callNumber==len(elevCalls)-1 and isdest:  #last call
            return srcFloor # stay at the same floor
        else:
            timeOfdrive = plusTime - elev.get_openTime() - elev.get_closeTime() - elev.get_startTime()
            if timeOfdrive>0:
                return srcFloor +  timeOfdrive * elev.get_speed()
            else:
                return srcFloor


    def get_callList(self, id:str=None) -> []:
        return self._callList.get(str(id))

    def addCall(self, id, call:Calls=None):
        if self._callList.get(id) == None:
            self._callList[str(id)] = []
        self._callList.get(id).append(call)

    def changDirc(self,elev:Elevator=None, dirction:str=None):
        if dirction!=None and elev!=None:
            self._direction[str(elev.get_id())] = dirction
    def get_Dirc(self,id:str=None) -> str:
        return self._direction[str(id)]