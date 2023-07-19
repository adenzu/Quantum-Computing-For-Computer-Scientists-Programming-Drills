import numpy as np

# Programming drill 2.4.3


def innerProduct(a: np.ndarray[complex], b: np.ndarray[complex]) -> complex:
    return np.dot((lambda x: x.conjugate())(a.T), b)


def norm(a: np.ndarray[complex]) -> float:
    return innerProduct(a, a).real ** 0.5


def distance(a: np.ndarray[complex], b: np.ndarray[complex]) -> float:
    return norm(a - b)


def main():
    # Create complex numbers
    c1 = complex(2, 3)
    c2 = complex(4, -1)
    c3 = complex(1, 0)

    # Create NumPy arrays of complex numbers
    arr1 = np.array([c1, c2, c3])
    arr2 = np.array([c3, c2, c1])

    # Test case 1: Compute distance between two arrays of complex numbers
    result1 = distance(arr1, arr2)
    print(result1)

    # Test case 2: Compute distance between two arrays of complex numbers with all real parts being zero
    arr3 = np.array([complex(0, 1), complex(0, 2), complex(0, 3)])
    arr4 = np.array([complex(0, 3), complex(0, 2), complex(0, 1)])
    result2 = distance(arr3, arr4)
    print(result2)

    # Test case 3: Compute distance between two arrays of complex numbers with all imaginary parts being zero
    arr5 = np.array([complex(1, 0), complex(2, 0), complex(3, 0)])
    arr6 = np.array([complex(3, 0), complex(2, 0), complex(1, 0)])
    result3 = distance(arr5, arr6)
    print(result3)


if __name__ == "__main__":
    main()
