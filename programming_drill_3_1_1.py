import numpy as np

# Programming drill 3.1.1


def getStateAfterOneClick(matrix: np.ndarray[bool], initialState: np.ndarray[int]) -> np.ndarray[int]:
    return np.matmul(matrix, initialState)


def getStateAfterTClicks(matrix: np.ndarray[bool], initialState: np.ndarray[int], t: int) -> np.ndarray[int]:
    result = initialState
    for i in range(t):
        result = getStateAfterOneClick(matrix, result)
    return result


def main():
    matrix = np.array([
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 1, 0],
    ], dtype=int)

    assert np.array_equal(getStateAfterOneClick(matrix, np.array(
        [6, 2, 1, 5, 3, 10])), np.array([0, 0, 12, 5, 1, 9]))
    print("Test passed!")
    assert np.array_equal(getStateAfterOneClick(matrix, np.array(
        [5, 5, 0, 2, 0, 15])), np.array([0, 0, 20, 2, 0, 5]))
    print("Test passed!")
    assert np.array_equal(getStateAfterTClicks(matrix, np.array(
        [0, 0, 27, 0, 0, 0]), 6), np.array([0, 0, 27, 0, 0, 0]))
    print("Test passed!")


if __name__ == "__main__":
    main()
