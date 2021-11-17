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
            c = Calls(arrive_time=row[1], src=row[2], dest=row[3])
            call_list.append(c)
            rows.append(row)
    return {"call_list": call_list, "rows_of_csv": rows}

def write_csv(allocated_list:[]=None, rows:[]=None):
    with open(r'C:\Users\Aviva\Desktop\output.csv', 'w', newline='') as f:
        print((allocated_list))
        writer = csv.writer(f)
        for i in range(len(allocated_list)):
            rows[i][5] = allocated_list[i]
        writer.writerows(rows)

