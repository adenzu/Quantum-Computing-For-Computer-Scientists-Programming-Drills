import numpy as np
import itertools as it


def vonNeumannEntropy(densityMatrix: np.ndarray[float]) -> float:
    eigenValues = np.linalg.eigvals(densityMatrix)
    return -np.sum(eigenValues * np.log2(eigenValues))


def getDensityOperator(stateVectors: np.ndarray[np.ndarray[complex]], probabilities: np.ndarray[float]) -> np.ndarray[complex]:
    return np.sum([probabilities[i] * np.outer(stateVectors[i], stateVectors[i]) for i in range(len(stateVectors))], axis=0)


def getDensityMatrix(stateVectors: np.ndarray[np.ndarray[complex]], probabilities: np.ndarray[float]) -> np.ndarray[float]:
    densityOperator = getDensityOperator(stateVectors, probabilities)
    zeroKet = np.array([1, 0], dtype=complex)
    oneKet = np.array([0, 1], dtype=complex)
    return np.vstack((densityOperator @ zeroKet, densityOperator @ oneKet))


def changeOfBasisMatrix(oldBasis: np.ndarray[np.ndarray[complex]], newBasis: np.ndarray[np.ndarray[complex]]) -> np.ndarray[complex]:
    return np.linalg.inv(newBasis) @ oldBasis


def diagonalizeDensityMatrix(densityMatrix: np.ndarray[float]) -> tuple[np.ndarray[float], np.ndarray[complex]]:
    eigenValues, eigenVectors = np.linalg.eig(densityMatrix)
    return np.diag(eigenValues), eigenVectors


def calculateComponentInBasis(stateVector1: np.ndarray[np.ndarray[complex]], stateVector2: np.ndarray[np.ndarray[complex]]) -> np.ndarray[complex]:
    return np.prod(np.abs(np.array([np.vdot(a, b) for a, b in zip(stateVector1, stateVector2)])))


def writeMessageInBasis(message: np.ndarray[np.ndarray[complex]], basis: np.ndarray[np.ndarray[complex]]) -> np.ndarray[np.ndarray[complex]]:
    zero = np.array([1, 0], dtype=complex)
    one = np.array([0, 1], dtype=complex)
    canonicalBasis = np.array([zero, one])
    changeOfBasis = changeOfBasisMatrix(canonicalBasis, basis)
    changeOfBasisOrignal = changeOfBasis.copy()
    messageTensored = message[0]
    for i in range(1, len(message)):
        changeOfBasis = np.kron(changeOfBasis, changeOfBasisOrignal)
        messageTensored = np.kron(messageTensored, message[i])
    return changeOfBasis @ messageTensored


def truncateMessage(message: np.ndarray[np.ndarray[complex]], basis: np.ndarray[np.ndarray[complex]], entropy: float) -> np.ndarray[np.ndarray[complex]]:
    messageInBasis = writeMessageInBasis(message, basis)
    n = len(message)
    correspondingVectors = np.array(list(it.product(basis.T, repeat=n)))
    E = 1e-2
    minProbability = 2 ** (-n * (entropy + E))
    maxProbability = 2 ** (-n * (entropy - E))
    for i in range(len(correspondingVectors)):
        correspondingVector = correspondingVectors[i]
        if not minProbability <= calculateComponentInBasis(message, correspondingVector) <= maxProbability:
            messageInBasis[i] = 0
    return messageInBasis


def main():
    # page 300

    zero = np.array([1, 0], dtype=complex)
    one = np.array([0, 1], dtype=complex)
    w1 = np.array([1, 1], dtype=complex) / np.sqrt(2)
    w2 = np.array([1, 0], dtype=complex)
    probabilities = np.array([1/3, 2/3])
    densityMatrix = getDensityMatrix(np.array([w1, w2]), probabilities)
    diagonalizedDensityMatrix, eigenVectors = diagonalizeDensityMatrix(
        densityMatrix)
    entropy = vonNeumannEntropy(densityMatrix)
    message = np.array([w1] * 8 + [w2] * 2)
    message = truncateMessage(message, eigenVectors, entropy)
    print('Density matrix:')
    print(densityMatrix)
    print('Diagonalized density matrix:')
    print(diagonalizedDensityMatrix)
    print('Entropy:')
    print(entropy)
    print('Message:')
    print(message)
    print('number of non-zero components:')
    print(np.count_nonzero(message))
    print(2**(10 * entropy.real))


if __name__ == '__main__':
    main()
