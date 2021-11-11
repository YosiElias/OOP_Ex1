import json
from Building import Building
from Elevator import Elevator
import ReadFromJson
from Manage import Manage
from Calls import Calls
import sys
import ReadCsv


if __name__ == '__main__':
    # b: Building = ReadFromJson.read('../venv/B3.json')
    # call_list = ReadCsv.read_csv(r"C:\Users\Aviva\Desktop\untitled2\venv\Calls_a.csv")
    # manag: Manage = Manage(b=b, callList=call_list)
    # print(b.get_maxFloor())
    ind = [1,3,1,3,3]
    i ={}
    index_elev_dict = {"3":"hjk", "1":"jnkl"}
    # for i in range(len(index_elev_dict)):
    #     i[str(index_elev_dict.keys())] = index_elev_dict.get(str(ind[i]))
    # print(ind)
    #
    j=0
    for key in index_elev_dict.keys():
        i[str(key)] = j
        j+=1
    print(i.get("3"))
    # print(a>str(8))
    # print(str(8)>a)

    # a={"1":"sfs", "2":5}
    # b=[1,2,3]
    # for i in b.__reversed__():
    #     print(b.index(i))
    # print(sys.maxsize)
    # c = Calls(arrive_time=1.0, src=0, dest=9)
    # manag.addCall("3", c)
    # c.add_src_time(1.5)
    # c.add_dst_time(11.5)
    # print(manag.getPos(id="3",time=10.9))