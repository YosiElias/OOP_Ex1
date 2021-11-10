import json
from Building import Building
from Elevator import Elevator
import ReadFromJson
from Manage import Manage
from Calls import Calls
import sys


if __name__ == '__main__':
    # b = ReadFromJson.read('../venv/B3.json')

    a={"1":"sfs", "2":5}
    b=[]
    for elev in a.keys():
        b.append(str(elev))
    print(sys.maxsize)
    # c = Calls(arrive_time=1.0, src=0, dest=9)
    # manag = Manage(b)
    # manag.addCall("3", c)
    # c.add_src_time(1.5)
    # c.add_dst_time(11.5)
    # print(manag.getPos(id="3",time=10.9))