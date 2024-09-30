import graph_data
import global_game_data
from numpy import random

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
    
    return path


def get_dfs_path():
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]
