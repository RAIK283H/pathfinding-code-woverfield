from graph_data import graph_data
import permutation


if __name__ == "__main__":
    permutations = permutation.getPermutations(len(graph_data[0]))
    hamiltonian = permutation.findHamiltonianCycles(graph_data[0], permutations)
    print("Permutations: ")
    print(permutations)
    print("Hamiltonian Cycles: ")
    print(hamiltonian)