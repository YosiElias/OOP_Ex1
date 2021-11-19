# Ex1 - the elevator mission - offline algorithm
![This is an image](https://user-images.githubusercontent.com/2201475/54477352-343e9b80-4807-11e9-9ee2-86595d06d702.png)


#### ID of presenters: 315858506,316156108

### Table of contents
* [Sources](#Sources)
* [Problem space](#Problem-space)
* [Classes structure](#Classes-structure)
* [Algorithm's principle](#Algorithm's-principle)
* [Algorithm structure](#Algorithm-structure)
* [Class diagram](#Class-diagram)
* [Results](#Results)

###  Sources
>[Source #1](https://softwareengineering.stackexchange.com/questions/331692/what-algorithm-is-used-by-elevators-to-find-the-shortest-path-to-travel-floor-or) - great answers to cut the total waiting times.

>[Source #2](https://www.cs.huji.ac.il/~ai/projects/2014/The_intelevator/files/report.pdf) - 
quality job which explaines the principle's of the elevator's movement and gave us good inspiration.

>[Source #3](https://www.i-programmer.info/programmer-puzzles/203-sharpen-your-coding-skills/4561-sharpen-your-coding-skills-elevator-puzzle.html?start=1) - also good principle's of the elevator's movement and emphasis to weak point on designing elevator's movement.


### Problem space
>We will notice that unlike the online situation, which there the calls are not given and we have no idea about the call details before it called, in the offline situation the whole calls are given to us, we have more data to work with. Therefore, the decision making can conider future data, so the calculate might be more complicated. Moreover, the position and the state of the elevator are not given to us, which means we had to calculate good estimate about them. Also, in this project we worked with files as json, so we had 'to exchange' in a good way the 'keys' to fiels into the classes that we create so we can use them.


### Classes structure
* data class - *Manage*- which manage the calls and the position of the elevators.
* Because we want to get accsess to the data in order to send the elevators in the optimal situation, we create class which manage the calls, when every elevator has it's own call list. This class serving the main algorithm class, giving call list in real time, position and more.
* algorithm class - *Offline*- which alocate every call in real time, and finally write the results to output file.
* Building class - *Building*- which recives the data from the json file and put it into the fitting fiels, and serving the offline class.
* Elevator class - *Elevator*- which recives the data from the json file and put it into the fitting fiels, and serving the offline class.
* Call class - *Calls*- which recives the data from the csv file and put it into the fitting fiels, and serving the offline class.


### Algorithm's principle
* With method 'alocate' we allocate the call to the fitting elevator. Every time we send the elevators to search, and select the best elevator with some calculate.
*  The algorithm runs couple of times by using 'filter': one time we send *all* elevators to the search, and one time we send only the elevaotrs with same direction to the direction of the current call, that before the source floor. If elevator is on the same direction but already passed the source floor, we didn't send it to the search, because we 'missed the floor'.
*  The calculate is considers 2 things: how much time it will take to reach the destination floor with the elevator, without considering the other calls that didn't finished yet, and might be on the elevator.The second thing is *'system time*- how much time the other calls in the elevator will delayed(if there are already other calls) if this elevator will take the call. We add those 2 together - the elevator with the lowest sum will be the chosen elevator.
*  The algorithm runs couple of times about the 'weight' of those 2 things. That means every time the algorithm will consider more or less in the things above(for example:one time the system time will double by 2 so it has more weight and in the other time it will be divided by 2. Of course it creates impact on the allocate).
*  Therefore, the algorithm runs couple of times, the best time will be the chosen and the alocate will be according to that. Finally, add the call to the call list of the elevator

### Algorithm's structure
* New call has come
* If the filter is 'on': send optimal elevators to search(same direction, and not passed)
* Else: send all elevators to search
* For all elevators: check best elevator(minimum 'cost to the system', as we said before)
* allocate the elevator and add the call to the elevtor's call list


### Class diagram
![This is an image](https://github.com/YosiElias/OOP_Ex1/blob/master/venv/UML%20Ex1%20OOP.png)

### Results
| Building/Calls| a                 |b                    |c                   |d                   |
| --------------|:-----------------:| -------------------:|-------------------:| ------------------:|
| B1            | aveTime:112, Uc=0 |                     |                    |                    |   
| B2            | aveTime:51, Uc=0  |                     |                    |                    |  
| B3            | aveTime:29, Uc=0  | aveTime:508, Uc=144 | aveTime:554, Uc=92 | aveTime:515, Uc=101|                        
| B4            | aveTime:17, Uc=0  | aveTime:183, Uc=15  | aveTime:189, Uc=0  | aveTime:175, Uc=0  |
| B5            | aveTime:11, Uc=0  | aveTime:38,  Uc=0   | aveTime:36, Uc=0   | aveTime:37 Uc=0    |
