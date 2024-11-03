import math
import unittest
from collections import deque
import graph_data    
import permutation
import global_game_data
from pathing import get_dfs_path, get_bfs_path


class TestPathFinding(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('test'.upper(), 'TEST')

    def test_isupper(self):
        self.assertTrue('TEST'.isupper())
        self.assertFalse('Test'.isupper())

    def test_floating_point_estimation(self):
        first_value = 0
        for x in range(1000):
            first_value += 1/100
        second_value = 10
        almost_pi = 3.1
        pi = math.pi
        self.assertNotEqual(first_value,second_value)
        self.assertAlmostEqual(first=first_value,second=second_value,delta=1e-9)
        self.assertNotEqual(almost_pi, pi)
        self.assertAlmostEqual(first=almost_pi, second=pi, delta=1e-1)

    def test_get_dfs_path0(self):
        global_game_data.current_graph_index = 0
        global_game_data.target_node = [0, 0, 1]
        expected = [0, 1, 2]
        result = get_dfs_path()
        self.assertEqual(expected, result)

    def test_get_bfs_path0(self):
        global_game_data.current_graph_index = 0
        global_game_data.target_node = [0, 0, 1]
        expected = [0, 1, 2]
        result = get_bfs_path()
        self.assertEqual(expected, result)

    def test_get_dfs_path1(self):
        global_game_data.current_graph_index = 1
        global_game_data.target_node = [0, 0, 1]
        expected = [0, 1, 2, 3]
        result = get_dfs_path()
        self.assertEqual(expected, result)

    def test_get_bfs_path1(self):
        global_game_data.current_graph_index = 1
        global_game_data.target_node = [0, 0, 1]
        expected = [0, 1, 2, 3]
        result = get_bfs_path()
        self.assertEqual(expected, result)

    def test_get_dfs_path2(self):
        global_game_data.current_graph_index = 2
        global_game_data.target_node = [0, 0, 1]
        expected = [0, 22, 20, 7, 12, 17, 18, 23, 21, 19, 1, 20, 22, 3, 11, 17, 18, 23]
        result = get_dfs_path()
        self.assertEqual(expected, result)

    def test_get_bfs_path2(self):
        global_game_data.current_graph_index = 2
        global_game_data.target_node = [0, 0, 1]
        expected = [0, 21, 19, 1, 19, 21, 23]
        result = get_bfs_path()
        self.assertEqual(expected, result)

class TestPermutationsHamiltonian(unittest.TestCase):
    def test_sjt0(self):
        perms = permutation.getPermutations(0)
        expected = []
        self.assertEqual(perms, expected)

    def test_sjt3(self):
        perms = permutation.getPermutations(3)
        expected = [[0, 1, 2], [0, 2, 1], [2, 0, 1], [2, 1, 0], [1, 2, 0], [1, 0, 2]]
        self.assertEqual(perms, expected)

    def test_hamiltonian_cycle(self):
        graphIndex = 1
        permutations = permutation.getPermutations(len(graph_data.hamiltonianGraphs[graphIndex]))
        hamiltonian = permutation.findHamiltonianCycles(graph_data.hamiltonianGraphs[graphIndex], permutations)
        expected = [[0, 1, 2], [2, 0, 1], [1, 2, 0]]
        self.assertEqual(hamiltonian, expected)

    def test_no_hamiltonian_cycle(self):
        graphIndex = 0
        permutations = permutation.getPermutations(len(graph_data.hamiltonianGraphs[graphIndex]))
        hamiltonian = permutation.findHamiltonianCycles(graph_data.hamiltonianGraphs[graphIndex], permutations)
        expected = []
        self.assertEqual(hamiltonian, expected)


if __name__ == '__main__':
    unittest.main()
