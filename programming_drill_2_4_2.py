import numpy as np

# Programming drill 2.4.2


def innerProduct(a: np.ndarray[complex], b: np.ndarray[complex]) -> complex:
    return np.dot((lambda x: x.conjugate())(a.T), b)


def norm(a: np.ndarray[complex]) -> float:
    return innerProduct(a, a).real ** 0.5


def main():
    # Create complex numbers
    cn1 = complex(2, 3)
    cn2 = complex(4, -1)
    cn3 = complex(1, 0)

    # Create NumPy arrays of complex numbers
    arr1 = np.array([cn1, cn2, cn3])

    # Test case 1: Compute norm of an array of complex numbers
    result1 = norm(arr1)
    print(result1)

    # Test case 2: Compute norm of an array of complex numbers with all real parts being zero
    arr2 = np.array([complex(0, 1), complex(0, 2), complex(0, 3)])
    result2 = norm(arr2)
    print(result2)

    # Test case 3: Compute norm of an array of complex numbers with all imaginary parts being zero
    arr3 = np.array([complex(1, 0), complex(2, 0), complex(3, 0)])
    result3 = norm(arr3)
    print(result3)

    # Test case 4: Compute norm of an empty array
    result4 = norm(np.array([]))
    print(result4)


if __name__ == "__main__":
    main()
