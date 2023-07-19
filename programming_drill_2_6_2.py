import numpy as np
# Programming drill 2.6.2


def adjoint(a: np.ndarray[complex]) -> np.ndarray[complex]:
    return (lambda x: x.conjugate())(a.T)


def isUnitary(a: np.ndarray[complex]) -> bool:
    return np.array_equal(np.identity(len(a)), np.matmul(a, adjoint(a)))


def main():
    # Test Case 1: Identity matrix
    a = np.eye(3, dtype=complex)  # 3x3 identity matrix
    print(isUnitary(a))  # Expected output: True

    # Test Case 2: Unitary matrix
    a = np.array([[0, 1j], [1j, 0]], dtype=complex)  # Unitary matrix
    print(isUnitary(a))  # Expected output: True

    # Test Case 3: Non-unitary matrix
    a = np.array([[1, 2], [3, 4]], dtype=complex)  # Non-unitary matrix
    print(isUnitary(a))  # Expected output: False

    # Test Case 4: Complex non-unitary matrix
    a = np.array([[1+2j, 3-1j], [0-1j, 2-3j]],
                 dtype=complex)  # Complex unitary matrix
    print(isUnitary(a))  # Expected output: False


if __name__ == "__main__":
    main()
