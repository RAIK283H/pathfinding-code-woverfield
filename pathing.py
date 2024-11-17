import graph_data
import global_game_data
from numpy import random
import heapq
import math

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    global_game_data.graph_paths.append(get_dijkstra_path())


def get_test_path():
    return graph_data.test_path[global_game_data.current_graph_index]


def get_random_path():
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    targetIdx = global_game_data.target_node[global_game_data.current_graph_index]
    startIdx = 0
    endIdx = len(graph) - 1
    currentIdx = startIdx

    assert 0 <= global_game_data.current_graph_index < len(graph_data.graph_data), "Graph index must be within graph_data"
    assert 0 <= global_game_data.target_node[global_game_data.current_graph_index] < len(graph), "Target node index must be within graph"


    path = []
    path.append(startIdx)

    def get_adjacent(nodeIndex):
        adjacencyList = graph[nodeIndex][1]
        randomIndex = random.choice(adjacencyList)
        return randomIndex
    
    while currentIdx != targetIdx:
        nextIdx = get_adjacent(currentIdx)
        path.append(nextIdx)
        currentIdx = nextIdx

    while currentIdx != endIdx:
        nextIdx = get_adjacent(currentIdx)
        path.append(nextIdx)
        currentIdx = nextIdx

    assert path[0] == startIdx, "Path must start at start index."
    assert targetIdx in path, "Path must hit target index."
    assert path[-1] == endIdx, "Path must end at end index."
    
    return path


def get_dfs_path():
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    startIdx = 0
    targetIdx = global_game_data.target_node[global_game_data.current_graph_index]
    endIdx = len(graph) - 1
    visited = set()

    def dfs(startNode, endNode):
        stack = [(startNode, [startNode])]

        while stack:
            currNode, path = stack.pop()

            if currNode in visited:
                continue
            
            visited.add(currNode)

            if currNode == endNode:
                return path

            for neighbor in sorted(graph[currNode][1]):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

        return None

    targetPath = dfs(startIdx, targetIdx)
    visited.clear()
    endPath = dfs(targetIdx, endIdx)

    assert targetIdx in targetPath, "Target node not found in the target path."

    fullPath = targetPath + endPath[1:]
    assert fullPath[-1] == endIdx, "Resulting path must end at the exit node."

    for i in range(len(fullPath) - 1):
        assert fullPath[i + 1] in graph[fullPath[i]][1], (
            f"Edge missing between {fullPath[i]} and {fullPath[i + 1]}"
        )

    return fullPath


from collections import deque

def get_bfs_path():
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    startIdx = 0
    targetIdx = global_game_data.target_node[global_game_data.current_graph_index]
    endIdx = len(graph) - 1

    def bfs(startNode, endNode):
        queue = deque([[startNode]])
        visited = set([startNode])

        while queue:
            currPath = queue.popleft()
            currNode = currPath[-1]

            if currNode == endNode:
                return currPath

            for neighbor in sorted(graph[currNode][1]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(currPath + [neighbor])

        return None

    targetPath = bfs(startIdx, targetIdx)
    endPath = bfs(targetIdx, endIdx)

    assert targetIdx in targetPath, "Target node not found in the target path."

    fullPath = targetPath + endPath[1:]
    assert fullPath[-1] == endIdx, "Resulting path must end at the exit node."

    for i in range(len(fullPath) - 1):
        assert fullPath[i + 1] in graph[fullPath[i]][1], (
            f"Edge missing between {fullPath[i]} and {fullPath[i + 1]}"
        )

    return fullPath


def get_dijkstra_path():
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    startIdx = 0
    targetIdx = global_game_data.target_node[global_game_data.current_graph_index]
    endIdx = len(graph) - 1

    def dijkstra(start, end):
        priorityQueue = [(0, start, [start])]
        distances = {node: float("inf") for node in range(len(graph))}
        distances[start] = 0

        while priorityQueue:
            currDistance, currNode, currPath = heapq.heappop(priorityQueue)

            if currNode == end:
                return currPath

            for neighbor in graph[currNode][1]:
                def calculate_distance(point1, point2):
                    x1, y1 = point1
                    x2, y2 = point2
                    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                newDistance = currDistance + calculate_distance(graph[currNode][0], graph[neighbor][0])
                if newDistance < distances.get(neighbor, float("inf")):
                    distances[neighbor] = newDistance
                    heapq.heappush(priorityQueue, (newDistance, neighbor, currPath + [neighbor]))

        return None
    
    targetPath = dijkstra(startIdx, targetIdx)
    if targetPath is None:
        return None

    endPath = dijkstra(targetIdx, endIdx)
    if endPath is None:
        return None


    path = targetPath + endPath[1:]

    assert path[0] == startIdx, "Path must start at start index."
    assert targetIdx in path, "Path must hit target index."
    assert path[-1] == endIdx, "Path must end at end index."

    return path

