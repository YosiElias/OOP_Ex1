from Building import Building
from Elevator import Elevator
from Calls import Calls
import math


class Manage:

    def __init__(self, b:Building=None, callList:[]=None):
        self._b = b
        self.callList = callList    #public variable
        self._elevDict = b.get_elevDict()
        self._callDict = {}
        for elev in b.get_elevDict().keys():    #init list for all the elevator
            self._callDict[str(b.get_elevDict().get(elev).get_id())] = []
        self._direction = {}

    def get_state(self,  id:str=None, time:float=0.0) -> str:
        """
        :return: "LEVEL"/"UP"/"DOWN"
        """
        elevCalls = self._callDict.get(str(id))  # list of Calls
        i = len(elevCalls) - 1
        for call in elevCalls.__reversed__():
            if call.get_time_dst() <= float(time) and i==len(elevCalls)-1: #the last call
                return "LEVEL"
                break
            elif call.get_time_dst() <= float(time):
                return call.get_dirc()
                break
            elif call.get_time_src() <= float(time):
                return call.get_dirc()
                break

    def numOfWaitCalls(self, id: str = None, time:float=0.0) -> int:
        callListOfElev =  self.get_callDict().get(id)
        if len(callListOfElev) == 0:
            return 0
        callCounter = 0
        for call in callListOfElev.__reversed__():
            if call.get_time_dst() <= float(time):
                return callCounter
            elif call.get_time_src() <= float(time):
                return callCounter + 1
            else:
                callCounter += 1
        return callCounter


    def getPos(self, id:str=None, time:float=0.0) -> int:
        """
        :param id: id of elev
        :param time: time to know where th elev is
        :return: where th elev is in time 'time'
        """
        floor = 0 # defulte of elevator before first move
        # if self._direction.get(id) == "UP":
        elevCalls = self._callDict.get(str(id)) #list of Calls
        i = len(elevCalls) - 1
        for call in elevCalls.__reversed__():
            if call.get_time_dst() <= float(time):
                floor = self.posFrom(srcFloor=call.get_dest(), plusTime=(float(time) - call.get_time_dst()), id=id, callNumber=i, isdest=True)
                break
            elif call.get_time_src() <= float(time):
                floor = self.posFrom(srcFloor=call.get_src(), plusTime=float(time) - call.get_time_src(), id=id, callNumber=i, isdest=False)
                break
        i = i-1
        return floor


    def posFrom(self, srcFloor:int=None, plusTime:float=None, id:str=None, callNumber:int=None, isdest:bool=None) ->float:
        """
        :rtype: float of floor get from srcFloor to time 'plusTime'
        """
        elev = self._elevDict.get(str(id))
        elevCalls = self._callDict.get(str(id))
        if callNumber==len(elevCalls)-1 and isdest:  #last call
            return srcFloor # stay at the same floor
        else:
            timeOfdrive = plusTime - elev.get_openTime() - elev.get_closeTime() - elev.get_startTime()
            if timeOfdrive>0:
                return int(srcFloor) +  float(timeOfdrive) * elev.get_speed()
            else:
                return srcFloor


    def get_callDict(self):
        return self._callDict

    def addCall(self, id, call):
        if self._callDict.get(id) == None:
            self._callDict[str(id)] = []
        self._callDict.get(id).append(call)
        src_time = self.calaulate_src_time(id=id, call=call)
        call.add_src_time(time=src_time)
        dest_time = self.calaulate_dest_time(id=id, call=call)
        call.add_dst_time(time=dest_time)

    def calaulate_src_time(self, id:str=None, call:Calls=None)-> float:
        """
        :return: the time to get to src of 'call'
        """
        elev:Elevator = self._elevDict.get(str(id))
        this_time = call.get_time_arrive()
        pos = self.getPos(id=id, time=this_time)
        floor = abs(int(pos) - int(call.get_src()))+1
        stop_time = elev.get_stopTime() + elev.get_openTime() + elev.get_closeTime() + elev.get_startTime()
        stops = self.numOfWaitCalls(id=id, time=this_time)
        # print("\nstops: ",stops)
        time = float(this_time) + float(floor)/float(elev.get_speed()) + float(stops)*float(stop_time)
        return time

    def calaulate_dest_time(self, id:str=None, call:Calls=None)-> float:
        """
        :return: the time to get to dest of 'call'
        """
        elev:Elevator = self._elevDict.get(str(id))
        this_time = call.get_time_src()
        pos = call.get_src()
        floor = abs(int(pos) - int(call.get_dest()))+1
        stop_time = elev.get_stopTime() + elev.get_openTime() + elev.get_closeTime() + elev.get_startTime()
        stops = self.numOfWaitCalls(id=id, time=this_time)
        time = this_time + floor/elev.get_speed() + stops*stop_time
        return time

    def changDirc(self,elev:Elevator=None, dirction:str=None):
        if dirction!=None and elev!=None:
            self._direction[str(elev.get_id())] = dirction
    def get_Dirc(self,id:str=None) -> str:
        return self._direction[str(id)]