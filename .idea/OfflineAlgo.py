import json
from Building import Building
from Elevator import Elevator
import ReadFromJson
from Manage import Manage
from Calls import Calls
import sys
import ReadCsv
####################################################
# temp value:
# calList = []
# c1 = Calls(arrive_time=1.0, src=0, dest=9)
# calList.append(c1)
# c2 = Calls(arrive_time=15.0, src=-10, dest=90)
# calList.append(c2)
# c3 = Calls(arrive_time=100.0, src=70, dest=90)
# calList.append(c3)
###################################################
class OfflineAlgo:

    def __init__(self, jsonPath:str=None, csvPath:str=None):
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
        print("**************************************** - RUN ALGORITEM IS DONE - ****************************************")


    def algoOffline(self):
        allocated_list = []
        for call in self.call_list:
            id = self.alocate(call)
            allocated_list.append(str(id))
            self.manage.addCall(id=id, call=call)
        for i in range(len(allocated_list)):
            allocated_list[i] = self.index_elev_dict.get(str(allocated_list[i]))
        # print(allocated_list)
        ReadCsv.write_csv(allocated_list=allocated_list, rows=self.rows_of_old_csv)

    def alocate(self, call:Calls=None)-> float:
        elevDic = self.b.get_elevDict()
        minCost = ["0", sys.maxsize]
        time = call.get_time_arrive()
        bestElev = self.getRelevantElev(call)
        if len(bestElev)==0:
            for id in elevDic.keys():
                bestElev.append(str(id))

        for id in elevDic.keys():
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
        return n * time


    def dist(self, id:str=None, call:Calls=None, elev:Elevator=None):
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
            if self.manage.get_state(id, time) == "LEVEL":
                bestElev.append(elev)
            elif call.get_dirc() == "UP" and self.manage.get_state(id, time) == "UP":
               elevPos = self.manage.getPos(id=id, time=call.get_time_arrive())
               if int(elevPos) < int(call.get_src()):
                   bestElev.append(elev)
            elif call.get_dirc() == "DOWN" and self.manage.get_state(id, time) == "DOWN":
               elevPos = self.manage.getPos(id=id, time=call.get_time_arrive())
               if int(elevPos) > int(call.get_src()):
                   bestElev.append(elev)

        return bestElev


if __name__ == '__main__':
    jsonPath = '../venv/B4.json'
    csvPath = r"C:\Users\Aviva\Desktop\untitled2\venv\Calls_a.csv"
    OfflineAlgo(jsonPath=jsonPath, csvPath=csvPath)

    # algoOffline(call_list=call_list)

























