import numpy as np

# Programming drill 4.1.1


def calculatePointProbability(ket: np.ndarray[complex], i: int) -> float:
    """
    calculate the probability of the i-th point
    :param ket: the state vector
    :param i: the i-th point
    :return: the probability of the i-th point
    """
    return abs(ket[i]) ** 2 / np.linalg.norm(ket) ** 2


def calculateTransitionAmplitude(
    ket1: np.ndarray[complex], ket2: np.ndarray[complex]
) -> complex:
    """
    calculate the transition amplitude from ket1 to ket2
    :param ket1: the start state vector
    :param ket2: the end state vector
    :return: the transition amplitude from ket1 to ket2
    """
    return np.vdot(ket2, ket1)


def main():
    # calculatePointProbability tests
    assert np.isclose(calculatePointProbability(np.array([1, 0, 0, 0]), 0), 1)
    assert np.isclose(calculatePointProbability(np.array([1, 0, 0, 0]), 1), 0)
    assert np.isclose(calculatePointProbability(
        np.array([1, 2, 3, 4]), 0), 1 / 30)
    print("calculatePointProbability tests passed")

    # calculateTransitionAmplitude tests
    assert np.isclose(
        calculateTransitionAmplitude(
            np.array([1, 0, 0, 0]), np.array([1, 0, 0, 0])), 1
    )
    assert np.isclose(
        calculateTransitionAmplitude(
            np.array([1, 0, 0, 0]), np.array([0, 1, 0, 0])), 0
    )
    assert np.isclose(
        calculateTransitionAmplitude(
            np.array([1, -1j]), np.array([1j, 1])), -2j
    )
    print("calculateTransitionAmplitude tests passed")


if __name__ == "__main__":
    main()
