import numpy as np
# Programming drill 2.6.1


def isHermitian(a: np.ndarray[complex]) -> bool:
    return np.array_equal(a, (lambda x: x.conjugate())(a.T))


def main():
    # Test Case 1: Hermitian Matrix
    matrix1 = np.array([[1+0j, 3-1j, 4+5j],
                        [3+1j, 2+0j, 6-3j],
                        [4-5j, 6+3j, 7+0j]])
    print(isHermitian(matrix1))  # Expected output: True

    # Test Case 2: Non-Hermitian Matrix
    matrix2 = np.array([[1+2j, 3+1j, 4+5j],
                        [3-1j, 2-1j, 6-3j],
                        [4-5j, 6+3j, 7+4j]])
    print(isHermitian(matrix2))  # Expected output: False

    # Test Case 3: Hermitian Matrix with Imaginary Zeros
    matrix3 = np.array([[1+0j, 3-1j, 0+0j],
                        [3+1j, 2+0j, 6-3j],
                        [0+0j, 6+3j, 7+0j]])
    print(isHermitian(matrix3))  # Expected output: True

    # Test Case 4: Hermitian Matrix with Real Numbers
    matrix4 = np.array([[1+0j, 3+0j, 4+0j],
                        [3+0j, 2+0j, 6+0j],
                        [4+0j, 6+0j, 7+0j]])
    print(isHermitian(matrix4))  # Expected output: True

    # Test Case 5: Empty Matrix
    matrix5 = np.array([])
    # Expected output: True (Empty matrix is considered Hermitian)
    print(isHermitian(matrix5))


if __name__ == "__main__":
    main()
