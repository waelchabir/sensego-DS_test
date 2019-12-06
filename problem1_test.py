"""
Script to automatically test your zombieCluster function
You should put the file of examples 'problem1_test.txt' in the same folder and run your 
script from that folder if your want to test automatically if your function is correct.
"""
import unittest
from ast import literal_eval
import numpy as np


def zombieCluster(matrix):
    #write your zombieCluster here
    #your function should return an int to be tested
    def searchConnectedZombies(matrix, lineIndex, cluster_elements):
        (_, nCol) = np.shape(matrix)
        result = cluster_elements
        for i in range(nCol):
            # Recursive call for search connected zombies if an element is not already included in the cluster
            if (matrix[lineIndex][i] == 1) and (lineIndex != i) and (i not in cluster_elements):
                result.append(i)
                connectedZombies = searchConnectedZombies(matrix, i, result)
                result = result + connectedZombies
        return result

    (nLine,nCol) = np.shape(matrix)
    lineIdx = 0
    nClusters = 0
    clusters_elements = []
    while lineIdx < nLine:
        clusters_elements.append(lineIdx)
        nClusters +=1
        current_cluster = [lineIdx]
        for colIdx in range(nCol):
            # look for all connections of the current zombie, make an exception for the diagonal elements
            if (matrix[lineIdx][colIdx] == 1) and (colIdx != lineIdx):
                current_cluster.append(colIdx)
                current_cluster = current_cluster + searchConnectedZombies(matrix, colIdx, current_cluster)
                clusters_elements = list(set(clusters_elements + current_cluster))
        print("Cluter " + str(nClusters) + " = " + str(set(current_cluster)))
        # search for an element not included in any cluster
        while(lineIdx in clusters_elements):
            lineIdx +=1
    return nClusters

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
            print("matrix " + str(i+1) + " total clusters= " + str(computed_res))
            with(self.subTest(i=i)):
                self.assertEqual(computed_res, self.values[i], msg.format(computed_res, self.values[i]))

if __name__ == '__main__':
    unittest.main()
