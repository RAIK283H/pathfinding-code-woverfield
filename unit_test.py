import math
import unittest
from collections import deque
import graph_data
import permutation
import global_game_data
from pathing import get_dfs_path, get_bfs_path, get_dijkstra_path
from f_w import adjacencyToMatrix, floydWarshall, buildPaths


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

class TestDijkstra(unittest.TestCase):
    def test_get_dijkstra_path_single(self):
        idx = 9
        target = 0

        global_game_data.current_graph_index = idx
        global_game_data.target_node = {idx: target}

        path = get_dijkstra_path()
        self.assertIsNotNone(path)
        self.assertEqual(path, [0])

    def test_get_dijkstra_path_no_path(self):
        idx = 10
        target = 3

        global_game_data.current_graph_index = idx
        global_game_data.target_node = {idx: target}

        path = get_dijkstra_path()
        self.assertEqual(path, None)

    def test_get_dijkstra_path(self):
        idx = 11
        target = 3

        global_game_data.current_graph_index = idx
        global_game_data.target_node = {idx: target}

        path = get_dijkstra_path()
        self.assertIsNotNone(path)
        self.assertTrue(path in [[0, 1, 3], [0, 2, 3]])

class TestFloydWarshall(unittest.TestCase):
    def test_floyd_warshall_basic(self):
        adjacencyList = {
            0: [(1, 3), (2, 8)],
            1: [(3, 1)],
            2: [(1, 4)],
            3: [(2, 7)],
        }

        n = 4
        graph_matrix = adjacencyToMatrix(adjacencyList, n)

        dist, parent = floydWarshall(graph_matrix)

        self.assertEqual(dist[0][3], 4)
        self.assertEqual(dist[1][2], 8)
        self.assertEqual(dist[0][2], 8)

        path = buildPaths(parent, 0, 3)
        self.assertEqual(path, [0, 1, 3])

    def test_floyd_warshall_negative_weights(self):
        adjacencyList = {
            0: [(1, 3)],
            1: [(2, -2)],
            2: [(3, 2)],
            3: [(0, -1)],
        }

        n = 4
        graph_matrix = adjacencyToMatrix(adjacencyList, n)

        dist, parent = floydWarshall(graph_matrix)

        self.assertEqual(dist[0][2], 1)
        self.assertEqual(dist[1][3], 0)

        path = buildPaths(parent, 0, 2)
        self.assertEqual(path, [0, 1, 2])

    def test_floyd_warshall_complete_graph(self):
        adjacencyList = {
            0: [(1, 1), (2, 2), (3, 3)],
            1: [(0, 1), (2, 1), (3, 2)],
            2: [(0, 2), (1, 1), (3, 1)],
            3: [(0, 3), (1, 2), (2, 1)],
        }

        n = 4
        graph_matrix = adjacencyToMatrix(adjacencyList, n)

        dist, parent = floydWarshall(graph_matrix)

        self.assertEqual(dist[0][3], 3)
        self.assertEqual(dist[1][2], 1)

        path = buildPaths(parent, 0, 3)
        self.assertEqual(path, [0, 3])

if __name__ == '__main__':
    unittest.main()
