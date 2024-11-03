import math

def getPermutations(n):
    if n < 2:
        return []

    perm = list(range(n))
    permutations = []
    directions = [-1] * n

    def getLargestMobile():
        mobile, mobile_index = -1, -1
        for i in range(n):
            if (directions[i] == -1 and i > 0 and perm[i] > perm[i - 1]) or (directions[i] == 1 and i < len(perm) - 1 and perm[i] > perm[i + 1]):
                if perm[i] > mobile:
                    mobile, mobile_index = perm[i], i
        return mobile_index

    while True:
        permutations.append(perm[:])

        mobile_index = getLargestMobile()
        if mobile_index == -1:
            break

        swap_index = mobile_index + directions[mobile_index]
        perm[mobile_index], perm[swap_index] = perm[swap_index], perm[mobile_index]
        directions[mobile_index], directions[swap_index] = directions[swap_index], directions[mobile_index]

        for i in range(len(perm)):
            if perm[i] > perm[swap_index]:
                directions[i] *= -1

    return permutations

def findHamiltonianCycles(graph, permutations):
    valid_cycles = []
    for perm in permutations:
        if isValidHamiltonian(graph, perm):
            valid_cycles.append(perm)
    return valid_cycles

def isValidHamiltonian(graph, perm):
    for i in range(len(perm) - 1):
        if perm[i + 1] not in graph[perm[i]][1]:
            return False
        if perm[0] not in graph[perm[-1]][1]:
            return False
    return True