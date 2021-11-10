import json
from Building import Building
from Elevator import Elevator

def read(filePath:str) -> Building:
    # Opening JSON file
    # f = open('../venv/B3.json')
    f = open(str(filePath))

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    minFloor = data['_minFloor']
    maxFloor = data['_maxFloor']
    elevList = data['_elevators']
    # print(maxFloor)
    b = Building(_minFloor=minFloor, _maxFloor=maxFloor)

    for elv in elevList:
        e = Elevator(id=elv['_id'], speed=elv['_speed'], minFloor=elv['_minFloor'], maxFloor=elv['_maxFloor'],
                     closeTime=elv['_closeTime'], openTime=elv['_openTime'],  startTime=elv['_startTime'],
                     stopTime=elv['_stopTime'])
        b+=e
        # print(b.get_elevDict()[str(e.get_id())])

    print(b)
    # Closing file
    f.close()
    return b



if __name__ == '__main__':
    b = read('../venv/B3.json')
    print(b.get_minFloor())
