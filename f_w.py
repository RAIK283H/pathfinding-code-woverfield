import math
import numpy as np

def adjacencyToMatrix(adjacencyList, n):
    matrix = np.full((n, n), math.inf)
    np.fill_diagonal(matrix, 0)

    for i in range(n):
        for neighbor, weight in adjacencyList[i]:
            matrix[i][neighbor] = weight
    
    return matrix

def floydWarshall(matrix):
    n = len(matrix)
    dist = matrix.copy()
    parent = np.full((n, n), -1)
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] < math.inf:
                parent[i][j] = i

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    parent[i][j] = parent[k][j]

    return dist, parent

def buildPaths(parent, start, end):
    path = []
    while end != -1:
        path.append(end)
        if end == start:
            return path[::-1]
        end = parent[start][end]
    
    return []
