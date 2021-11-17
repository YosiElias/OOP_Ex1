import json
from Building import Building
from Elevator import Elevator

def read(filePath:str) -> Building:
    # Opening JSON file
    f = open(str(filePath))

    # returns JSON object as a dictionary
    data = json.load(f)

    # Iterating through the json
    minFloor = data['_minFloor']
    maxFloor = data['_maxFloor']
    elevList = data['_elevators']
    b = Building(_minFloor=minFloor, _maxFloor=maxFloor)

    for elv in elevList:    # build all elevators
        e = Elevator(id=elv['_id'], speed=elv['_speed'], minFloor=elv['_minFloor'], maxFloor=elv['_maxFloor'],
                     closeTime=elv['_closeTime'], openTime=elv['_openTime'],  startTime=elv['_startTime'],
                     stopTime=elv['_stopTime'])
        b+=e    # We override the 'add' operation to get more comfortable and clean code

    f.close()
    return b  # Building


