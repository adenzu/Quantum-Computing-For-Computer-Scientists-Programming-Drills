import numpy as np
import matplotlib.pyplot as plt

# Programming drill 4.3.1


def getEigenValuesAndVectors(observableMatrix: np.ndarray[complex]) -> tuple[np.ndarray[complex], np.ndarray[complex]]:
    return np.linalg.eig(observableMatrix)


def calculateMeanValueOfObservable(observedMatrix: np.ndarray[complex], stateVector: np.ndarray[complex]) -> complex:
    return stateVector.T @ observedMatrix @ stateVector


def calculateEigenvectorTransitionProbability(stateVector: np.ndarray[complex], eigenVector: np.ndarray[complex]) -> float:
    normalizedStateVector = stateVector / np.linalg.norm(stateVector)
    return np.abs(eigenVector.T @ normalizedStateVector) ** 2


def calculateAllEigenvectorTransitionProbabilities(stateVector: np.ndarray[complex], eigenVectors: np.ndarray[complex]) -> np.ndarray[float]:
    return np.array([calculateEigenvectorTransitionProbability(stateVector, eigenVector) for eigenVector in eigenVectors])


def plotEigenvectorTransitionProbabilities(stateVector: np.ndarray[complex], eigenVectors: np.ndarray[complex]) -> None:
    probabilities = calculateAllEigenvectorTransitionProbabilities(
        stateVector, eigenVectors)
    plt.bar(np.arange(len(probabilities)), probabilities)
    plt.show()


def main():
    # example 4.3.1
    stateVector = np.array([1, 1], dtype=complex) / 2
    observableMatrix = np.array([[-1, -1j], [1j, 1]], dtype=complex)

    eigenValues, eigenVectors = getEigenValuesAndVectors(observableMatrix)

    assert np.allclose(observableMatrix @
                       eigenVectors[:, 0], eigenValues[0] * eigenVectors[:, 0])
    assert np.allclose(observableMatrix @
                       eigenVectors[:, 1], eigenValues[1] * eigenVectors[:, 1])

    print("Eigenvalues:")
    print(eigenValues)
    assert np.allclose(eigenValues, np.array([-np.sqrt(2), np.sqrt(2)]))

    print("Eigenvectors:")
    print(eigenVectors)
    print(eigenVectors[:, 0])
    print(eigenVectors[:, 1])

    # it finds different eigenvectors than the book i don't know why
    # assert np.allclose(eigenVectors, np.array([[-0.923j, -0.382], [-0.382j, 0.923]]))

    probabilities = calculateAllEigenvectorTransitionProbabilities(
        stateVector, eigenVectors)
    meanValue = eigenValues @ probabilities

    print("Mean value:")
    print(meanValue)
    assert np.isclose(meanValue, 0)

    assert np.isclose(meanValue, calculateMeanValueOfObservable(
        observableMatrix, stateVector))

    print("Test passed.")

    plotEigenvectorTransitionProbabilities(stateVector, eigenVectors)


if __name__ == "__main__":
    main()
