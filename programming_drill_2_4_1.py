import numpy as np

# Programming drill 2.4.1


def innerProduct(a: np.ndarray[complex], b: np.ndarray[complex]) -> complex:
    return np.dot((lambda x: x.conjugate())(a.T), b)


def main():
    # Create complex numbers
    cn1 = complex(2, 3)
    cn2 = complex(4, -1)
    cn3 = complex(1, 0)
    cn4 = complex(0, 5)

    # Create NumPy arrays of complex numbers
    arr1 = np.array([cn1, cn2, cn3])
    arr2 = np.array([cn3, cn4, cn1])

    # Test case 1: Multiply two arrays of complex numbers
    result1 = innerProduct(arr1, arr2)
    print(result1)

    # Test case 2: Multiply array of complex numbers with itself
    result2 = innerProduct(arr1, arr1)
    print(result2)


if __name__ == "__main__":
    main()
