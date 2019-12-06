"""
Script to automatically test your zombieCluster function
You should put the file of examples 'problem1_test.txt' in the same folder and run your 
script from that folder if your want to test automatically if your function is correct.
"""
import unittest
from ast import literal_eval


def zombieCluster(matrix):
    #write your zombieCluster here
    #your function should return an int to be tested
    return 1

class test_problem(unittest.TestCase):
    """
    Class to test the values provided by zombieCluster if an integration is done
    """
    def setUp(self):
        self.matrices = []
        self.values = []
        with open('problem1_test.txt', 'r') as file:
            line = file.readline()
            while (line):
                if ('example' in line):
                    temp = ''
                elif ('[' in line):
                    temp += line
                elif ('result' in line):
                    self.matrices.append(literal_eval(temp))
                    self.values.append(int(line.split(' = ')[1]))
                line = file.readline()
        self.n_tests = len(self.values)
        assert self.n_tests==len(self.matrices), "problem reading file, check it has not been modified or corrupted"

    def test_zombieCluster(self):
        msg = 'wrong value computed. zombieCluster returned {} when expected {}'
        for i in range(self.n_tests):
            computed_res = zombieCluster(self.matrices[i])
            with(self.subTest(i=i)):
                self.assertEqual(computed_res, self.values[i], msg.format(computed_res, self.values[i]))

if __name__ == '__main__':
    unittest.main()
