import json
from Building import Building
from Elevator import Elevator
import ReadFromJson
from Manage import Manage
from Calls import Calls
import sys
####################################################
#temp value:
calList = []
c1 = Calls(arrive_time=1.0, src=0, dest=9)
calList.append(c1)
c2 = Calls(arrive_time=15.0, src=-10, dest=90)
calList.append(c2)
c3 = Calls(arrive_time=100.0, src=70, dest=90)
calList.append(c3)
###################################################
b = ReadFromJson.read('../venv/B3.json')
manage = Manage(b)

def alocate(call:Calls=None)-> float:
    minCost = ["0", sys.maxsize]
    time = call.get_time_arrive()
    bestElev = getRelevantElev(call)
    if len(bestElev)==0:
        for id in elevDic.keys():
            bestElev.append(str(id))
    for id in elevDic.keys():
        elev = elevDic.get(str(id))
        dist = dist(id=id, call=call, elev=elev) #Time that will take to make the call 'DONE'
        timeCost = systemTime(id=id, call=call, elev=elev) #In how many time the other calls in the elevator will be delayed
        timeCost += dist    #Together- the total time to the system
        if timeCost < minCost[1]:
            minCost[0] = str(id)
            minCost[1] = timeCost

    return str(minCost[0]);


def systemTime(id:str=None, call:calls=None, elev:Elevator=None):
    # n = manage.numOfWaitCalls(id, b.get_minFloor(), b.get_maxFloor()) #Todo
    time = elev.get_startTime() + elev.get_stopTime() + elev.get_closeTime() + elev.get_openTime()
    return n * time




def dist(id:str=None, call:calls=None, elev:Elevator=None):
    pos = manage.getPos(id=id, time=call.get_time_arrive())
    amountFloor = abs(call.get_src() - call.get_dest())+1
    comeCall =  abs(call.get_src() - pos)+1
    speedFloor = 1.0/elev.get_speed()
    speedCallStart = speedFloor * amountFloor
    speedCall = speedFloor * comeCall
    slowing = elev.get_closeTime() + (elev.get_openTime() * 2) + elev.get_stopTime() + elev.get_startTime()
    return speedCall + speedCallStart + slowing




def getRelevantElev(call:Calls=None)-> []:
    bestElev = []
    elevDic = b.get_elevDict()
    time = call.get_time_arrive()

    for id in elevDic.keys():
        elev = elevDic.get(str(id))
        if manage.get_state(id, time) == "LEVEL":
            bestElev.append(elev)
        elif call.get_dirc() == "UP" and manage.get_state(id, time) == "UP":
           elevPos = manage.getPos(id=id, time=call.get_time_arrive())
           if elevPos < call.get_src():
               bestElev.append(elev)
        elif call.get_dirc() == "DOWN" and manage.get_state(id, time) == "DOWN":
           elevPos = manage.getPos(id=id, time=call.get_time_arrive())
           if elevPos > call.get_src():
               bestElev.append(elev)

    return bestElev


if __name__ == '__main__':
    for call in calList:
        alocate(call)
























