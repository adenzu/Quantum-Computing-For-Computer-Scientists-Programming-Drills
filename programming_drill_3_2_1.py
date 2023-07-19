import numpy as np

# Programming drill 3.2.1


def getStateAfterOneClick(matrix: np.ndarray[float], initialState: np.ndarray[int]) -> np.ndarray[int]:
    return np.matmul(matrix, initialState)


def getStateAfterTClicks(matrix: np.ndarray[float], initialState: np.ndarray[int], t: int) -> np.ndarray[int]:
    result = initialState
    for _ in range(t):
        result = getStateAfterOneClick(matrix, result)
    return result


def main():
    matrix = np.array([
        [0, 0.5, 0.5, 0],
        [0.5, 0, 0, 0.5],
        [0.5, 0, 0, 0.5],
        [0, 0.5, 0.5, 0],
    ], dtype=float)

    assert np.array_equal(getStateAfterOneClick(
        matrix, np.array([1, 0, 0, 0])), np.array([0, 0.5, 0.5, 0]))
    print("Test passed!")
    assert np.array_equal(getStateAfterOneClick(
        matrix, np.array([0, 0.5, 0.5, 0])), np.array([0.5, 0, 0, 0.5]))
    print("Test passed!")
    assert np.array_equal(getStateAfterOneClick(
        matrix, np.array([0.5, 0, 0, 0.5])), np.array([0, 0.5, 0.5, 0]))
    print("Test passed!")
    assert np.array_equal(getStateAfterTClicks(
        matrix, np.array([1, 0, 0, 0]), 2), np.array([0.5, 0, 0, 0.5]))
    print("Test passed!")


if __name__ == "__main__":
    main()
