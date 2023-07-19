import numpy as np

# Programming drill 3.3.1


def getStateAfterOneClick(matrix: np.ndarray[complex], initialState: np.ndarray[int]) -> np.ndarray[int]:
    return np.matmul(matrix, initialState)


def getStateAfterTClicks(matrix: np.ndarray[complex], initialState: np.ndarray[int], t: int) -> np.ndarray[int]:
    result = initialState
    for _ in range(t):
        result = getStateAfterOneClick(matrix, result)
    return result


def main():
    matrixU = np.array([
        [1 / np.sqrt(2), 1 / np.sqrt(2), 0],
        [-1j / np.sqrt(2), 1j / np.sqrt(2), 0],
        [0, 0, 1j],
    ], dtype=complex)

    stateX = np.array([1 / np.sqrt(3), 2j / np.sqrt(15), np.sqrt(2 / 5)])
    stateY = np.array([(np.sqrt(5) + 2j) / np.sqrt(30),
                      (-2 - np.sqrt(5) * 1j) / np.sqrt(30), np.sqrt(2 / 5) * 1j])

    stateUX = getStateAfterOneClick(matrixU, stateX)

    assert np.allclose(stateUX, stateY, atol=1e-15)
    print("Test passed!")


if __name__ == "__main__":
    main()
