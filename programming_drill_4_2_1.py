import numpy as np

# Programming drill 4.2.1


def isHermitian(matrix: np.ndarray[complex]) -> bool:
    return np.allclose(matrix, matrix.conj().T)


def calculateMeanValueOfObservable(
    observableMatrix: np.ndarray[complex],
    stateVector: np.ndarray[complex],
) -> complex:
    if isHermitian(observableMatrix):
        try:
            return stateVector.conj().T @ observableMatrix @ stateVector
        except ValueError:
            raise ValueError(
                "The dimensions of the observable matrix and the state vector do not match."
            )
    else:
        raise ValueError("The observable matrix is not Hermitian.")


def demeanObservable(
    observableMatrix: np.ndarray[complex],
    stateVector: np.ndarray[complex],
) -> np.ndarray[complex]:
    return observableMatrix - calculateMeanValueOfObservable(
        observableMatrix, stateVector
    ) * np.identity(observableMatrix.shape[0])


def calculateVarianceOfObservable(
    observableMatrix: np.ndarray[complex],
    stateVector: np.ndarray[complex],
) -> complex:
    demeanedObservable = demeanObservable(observableMatrix, stateVector)
    return calculateMeanValueOfObservable(
        demeanedObservable @ demeanedObservable, stateVector
    )


def main():
    # example 4.2.7
    observableMatrix = np.array([[1, -1j], [1j, 2]], dtype=complex)
    stateVector = np.array([1, 1j], dtype=complex) / np.sqrt(2)
    observableVariance = calculateVarianceOfObservable(
        observableMatrix, stateVector)
    assert np.isclose(observableVariance, 0.25)
    print("Test passed.")


if __name__ == "__main__":
    main()
