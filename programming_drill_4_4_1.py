import numpy as np

# Programming drill 4.4.1


def main():
    # n many unitary matrices
    unitaryMatrix1 = np.array([[0, 1], [1, 0]], dtype=complex)
    unitaryMatrix2 = np.array([[1, 0], [0, -1]], dtype=complex)
    unitaryMatrix3 = np.array(
        [[1, 0], [0, np.exp(1j * np.pi / 4)]], dtype=complex)
    unitaryMatrix4 = np.array(
        [[np.exp(1j * np.pi / 4), 0], [0, np.exp(1j * np.pi / 4)]], dtype=complex)

    stateVector = np.array([1, 0], dtype=complex)

    # n steps
    result = unitaryMatrix4 @ unitaryMatrix3 @ unitaryMatrix2 @ unitaryMatrix1 @ stateVector

    print(result)


if __name__ == "__main__":
    main()
