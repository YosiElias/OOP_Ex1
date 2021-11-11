import csv
import json
from Building import Building
from Elevator import Elevator
from Calls import Calls
from Manage import Manage

def read_csv(path: str) -> {}:
    rows = []
    call_list = []

    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            c = Calls(arrive_time=row[1], src=row[2], dest=row[3]) #just_call=row[0], ,assigning=row[4]
            call_list.append(c)
            rows.append(row)
    # print(type(reader))
    # print((rows))
    return {"call_list": call_list, "rows_of_csv": rows}

def write_csv(allocated_list:[]=None, rows:[]=None):      # path_new_csv: str=None, path_old_csv: str=None,
    with open('output.csv', 'w', newline='') as f:     #'w'
        # print(len(allocated_list))
        writer = csv.writer(f)  #  quoting=csv.QUOTE_ALL
        for i in range(len(allocated_list)):       #row, ans        rows
            rows[i][5] = allocated_list[i]    #check if this loop legal
        writer.writerows(rows)


if __name__ == '__main__':
    call_list = read_csv(r"C:\Users\Aviva\Desktop\untitled2\venv\Calls_a.csv")  #-----return Dict!!!-------
    # print(d.get_full_call(d,3).get_src())
    # m = Manage()
    # print(m.callList)
    #
    #
    # print(call_list[0])
    # m= Manage
    # m.get_full_call()