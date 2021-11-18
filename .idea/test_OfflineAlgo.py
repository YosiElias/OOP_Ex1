import unittest
import csv
from OfflineAlgo import OfflineAlgo



class TestOfflineAlgo(unittest.TestCase):
    """
    Checks that the algorithm makes a logical insertion,
    based on a preliminary look at the case and an in-depth analysis of what the best placement is.
    """
    def test_allocate(self):
        outputPath = r"C:\Users\Aviva\Desktop\output.csv"
        with open(outputPath) as f:
            reader = csv.reader(f)
            i=0
            id =[]
            for row in reader:
                id.append(row[5])
                i+=1
                if i==2:
                    break
        self.assertEqual(id[0], '1')
        self.assertEqual(id[1], '1')

    def test_numOfWaitCalls(self):
        """
        Checking the function that needs to return some calls will be delayed if I added a call at a certain time.
        We expect the function to return the total calls it received during the entire
        run because the time given to it is 0.0 and if we add a call at this time
        we will drag a delay to all the calls received during the entire run.
        """
        jsonPath = r'C:\Users\Aviva\Desktop\B3.json'
        csvPath = r"C:\Users\Aviva\Desktop\Calls_b.csv"
        outputPath = r"C:\Users\Aviva\Desktop\output.csv"
        algo = OfflineAlgo(jsonPath=jsonPath, csvPath=csvPath, N_MULL_OF_COST=1.7000000000000002, FILTER=1)

        with open(outputPath) as f:
            reader = csv.reader(f)
            i=0
            id =[]
            for row in reader:
                if row[5] == '0':
                    i+=1

        self.assertEqual(algo.manage.numOfWaitCalls(id=3, time=0.0), i)


if __name__ == '__main__':
    unittest.main()
