import numpy as np

"""
Programming Drill 10.2.1 Write a program that lets the user choose how many qubits
the alphabet of the quantum source consists of, enter the probability associated with
each qubit, and compute von Neumann entropy as well as the orthonormal basis for
the associated density matrix.

Programmer's note:
There are some unclear points in the problem statement (to me at least). 

    By the part "choose how many qubits the alphabet of the quantum source consists of" I assume the 
    user chooses the number of the possible 'letters' in the alphabet, and their respective
    values and probabilities. It could also interpreted as a letter being able to be 
    represented by variable number of qubits, but I don't think that's the case since 
    the author of the book has not introduced such a concept yet. In either case I think
    the user has to enter the values for the qubits, and their probabilities. 
"""


def getDensityOperator(stateVectors: np.ndarray[np.ndarray[complex]], probabilities: np.ndarray[float]) -> np.ndarray[complex]:
    return np.sum([probabilities[i] * np.outer(stateVectors[i], stateVectors[i]) for i in range(len(stateVectors))], axis=0)


def computeVonNeumannEntropy(densityMatrix: np.ndarray[float]) -> float:
    eigenValues = np.linalg.eigvals(densityMatrix)
    return -np.sum(eigenValues * np.log2(eigenValues))


def computeDensityMatrix(stateVectors: np.ndarray[np.ndarray[complex]], probabilities: np.ndarray[float]) -> np.ndarray[float]:
    densityOperator = getDensityOperator(stateVectors, probabilities)
    zeroKet = np.array([1, 0], dtype=complex)
    oneKet = np.array([0, 1], dtype=complex)
    return np.vstack((densityOperator @ zeroKet, densityOperator @ oneKet))


def main():
    # Test case 1
    stateVectors = np.array([np.array([1, 1], dtype=complex) / np.sqrt(
        2), np.array([1, -1], dtype=complex) / np.sqrt(2)])
    probabilities = np.array([1/4, 3/4])
    densityMatrix = computeDensityMatrix(stateVectors, probabilities)
    entropy = computeVonNeumannEntropy(densityMatrix)
    densityMatrixOrthonormalBasis = np.linalg.eig(densityMatrix)[1]
    print("Test case 1:")
    print("Density matrix:")
    print(densityMatrix)
    print("Von Neumann entropy:")
    print(entropy)
    print("Orthonormal basis for the density matrix:")
    print(densityMatrixOrthonormalBasis)

    # Test case 2 from example 10.2.4
    stateVectors = np.array(
        [np.array([1, 1], dtype=complex) / np.sqrt(2), np.array([1, 0], dtype=complex)])
    probabilities = np.array([1/3, 2/3])
    densityMatrix = computeDensityMatrix(stateVectors, probabilities)
    entropy = computeVonNeumannEntropy(densityMatrix)
    densityMatrixOrthonormalBasis = np.linalg.eig(densityMatrix)[1]
    print("Test case 2:")
    print("Density matrix:")
    print(densityMatrix)
    print("Von Neumann entropy:")
    print(entropy)
    print("Orthonormal basis for the density matrix:")
    print(densityMatrixOrthonormalBasis)


if __name__ == '__main__':
    main()
