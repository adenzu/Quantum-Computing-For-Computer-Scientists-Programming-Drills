import numpy as np

# Programming drill 2.7.1


def tensorProduct(a: np.ndarray[complex], b: np.ndarray[complex], /) -> np.ndarray:
    return np.tensordot(a, b, axes=0)


def main():

    # Test Case 1
    a = np.array([1+2j, 3+4j])
    b = np.array([5+6j, 7+8j])
    result = tensorProduct(a, b)
    print(result)

    # Test Case 2
    a = np.array([2+3j, 4+5j])
    b = np.array([6+7j, 8+9j])
    result = tensorProduct(a, b)
    print(result)

    # Test Case 3
    a = np.array([1+1j, 1-1j])
    b = np.array([2+2j, 2-2j])
    result = tensorProduct(a, b)
    print(result)


if __name__ == "__main__":
    main()
