import json
from Building import Building
from Elevator import Elevator
import ReadFromJson
from Manage import Manage
from Calls import Calls
import sys
import ReadCsv
import numpy as np
####################################################
# This is an offline model that aims to bring back the best elevator placement for any scenario.
#
# This is where the main calculation and management of the algorithm takes place,
# the algorithm receives as a parameter the "degree of generosity" (between 0.9 and 3.5),
# and the filter parameter that decides whether to apply a filter on the elevators to the most relevant elevators
# for reading and only then compare, or search among all elevators. (filter off  when = 1).
#
# Finally in the main function we choose from all the parameters the best parameters for the relevant scenario and building.
# We can do this because it is an offline algorithm.
###################################################


class OfflineAlgo:

    def __init__(self, jsonPath:str=None, csvPath:str=None, N_MULL_OF_COST:float=1.0, FILTER:int=0):
        self.N_MULL_OF_COST = N_MULL_OF_COST
        self.FILTER = FILTER
        self.b: Building = ReadFromJson.read(jsonPath)
        self.index_elev_dict = {}
        j=0
        for key in self.b.get_elevDict().keys():
            self.index_elev_dict[str(key)] = j
            j+=1
        csv_dict:{} = ReadCsv.read_csv(csvPath)
        self.call_list = csv_dict.get("call_list")
        self.rows_of_old_csv = csv_dict.get("rows_of_csv")
        self.manage: Manage = Manage(b=self.b, callList=self.call_list)
        self.algoOffline()

        print("****************************************  RUN ALGORITEM IS DONE :) ****************************************")


    def algoOffline(self):
        allocated_list = []
        for call in self.call_list:
            id = self.alocate(call)
            allocated_list.append(str(id))
            self.manage.addCall(id=id, call=call)
        for i in range(len(allocated_list)):
            allocated_list[i] = self.index_elev_dict.get(str(allocated_list[i]))
        ReadCsv.write_csv(allocated_list=allocated_list, rows=self.rows_of_old_csv)

    def alocate(self, call:Calls=None)-> float:
        elevDic = self.b.get_elevDict()
        minCost = ["0", sys.maxsize]
        time = call.get_time_arrive()
        if self.FILTER==0:
            bestElev = self.getRelevantElev(call)
        else:
            bestElev = []
        if len(bestElev)==0:
            for id in elevDic.keys():
                bestElev.append(str(id))

        for id in bestElev:
            elev = elevDic.get(str(id))
            dis = self.dist(id=id, call=call, elev=elev) #Time that will take to make the call 'DONE'
            timeCost = self.systemTime(id=id, call=call, elev=elev) #In how many time the other calls in the elevator will be delayed
            timeCost += dis    #Together- the total time to the system
            if timeCost < minCost[1]:
                minCost[0] = str(id)
                minCost[1] = timeCost

        return str(minCost[0]);


    def systemTime(self, id:str=None, call:Calls=None, elev:Elevator=None):
        n = self.manage.numOfWaitCalls(id=id, time=call.get_time_arrive())
        time = elev.get_startTime() + elev.get_stopTime() + elev.get_closeTime() + elev.get_openTime()
        return n * time *self.N_MULL_OF_COST


    def dist(self, id:str=None, call:Calls=None, elev:Elevator=None):
        elevCalls = self.manage._callDict.get(str(id))
        pos = self.manage.getPos(id=id, time=call.get_time_arrive())
        amountFloor = abs(int(call.get_src()) - int(call.get_dest()))+1
        comeCall =  abs(int(call.get_src()) - int(pos))+1
        speedFloor = 1.0/elev.get_speed()
        speedCallStart = speedFloor * amountFloor
        speedCall = speedFloor * comeCall
        slowing = elev.get_closeTime() + (elev.get_openTime() * 2) + elev.get_stopTime() + elev.get_startTime()
        return speedCall + speedCallStart + slowing




    def getRelevantElev(self, call:Calls=None)-> []:
        bestElev = []
        elevDic = self.b.get_elevDict()
        time = call.get_time_arrive()

        for id in elevDic.keys():
            elev = elevDic.get(str(id))
            state = self.manage.get_state(id, time)
            if  state == "LEVEL":
                bestElev.append(elev.get_id())
            elif call.get_dirc() == "UP" and state == "UP":
               elevPos = self.manage.getPos(id=id, time=call.get_time_arrive())
               if int(elevPos) < int(call.get_src()):
                   bestElev.append(elev.get_id())
            elif call.get_dirc() == "DOWN" and state == "DOWN":
               elevPos = self.manage.getPos(id=id, time=call.get_time_arrive())
               if int(elevPos) > int(call.get_src()):
                   bestElev.append(elev.get_id())

        return bestElev

    def avarage_time_wait(self)->float:
        time = 0.0
        for call in self.call_list:
            if float(call.get_time_dst()) <= float(self.call_list[-1].get_time_dst())-1000:# -1000 to 'normlaze' the time to be more realy
                time +=  (float(call.get_time_dst()) - float(call.get_time_arrive()))
        print("Avarage for ",self.N_MULL_OF_COST, "is: ",time / len(self.call_list))
        return time/len(self.call_list)



if __name__ == '__main__':

    jsonPath = r'C:\Users\Aviva\Desktop\B3.json'
    csvPath = r"C:\Users\Aviva\Desktop\Calls_b.csv"

    algo = OfflineAlgo(jsonPath=jsonPath, csvPath=csvPath, N_MULL_OF_COST=1.0,  FILTER=0)
    maxAvg = algo.avarage_time_wait()
    bestfilter = 0
    max_n = 1.0
    n=0.9
    while n < 3.55:
        for filter in [0,1]:    #0= with filter. 1= without filter
            algo = OfflineAlgo(jsonPath=jsonPath, csvPath=csvPath, N_MULL_OF_COST=n, FILTER=filter)
            tempAvg = algo.avarage_time_wait()
            if (tempAvg < maxAvg):
                maxAvg = tempAvg
                max_n = n
                bestfilter = filter
            n += 0.8


    algo = OfflineAlgo(jsonPath=jsonPath, csvPath=csvPath, N_MULL_OF_COST=max_n, FILTER=bestfilter)
    print("Best n: ",max_n,"Best FILTER: ",bestfilter ,"AVG: ",algo.avarage_time_wait())
























