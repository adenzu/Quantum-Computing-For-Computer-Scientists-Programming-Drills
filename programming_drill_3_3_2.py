import numpy as np


# no parameter for probability of slit to target movement because i dont like it
def generateMultislitExperimentMatrix(
    numberOfSlits: int,
    numberOfTargetsPerSlit: int,
) -> np.ndarray[complex]:
    # initial vertex: 1
    # number of slit vertices: numberOfSlits
    # number of target vertices: numberOfSlits * numberOfTargetsPerSlit - numberOfSlits + 1
    totalNumberOfVertices = numberOfSlits * numberOfTargetsPerSlit + 2
    matrix = np.zeros((totalNumberOfVertices, totalNumberOfVertices), dtype=complex)

    slitProbability = 1 / numberOfSlits
    targetProbability = 1 / numberOfTargetsPerSlit

    a = 1 / np.sqrt(6)
    b = (targetProbability - a * a) ** 0.5

    firstTargetNumber = -a + b * 1j
    lastTargetNumber = a - b * 1j
    remainingTargetNumber = a + b * 1j

    for i in range(1, 1 + numberOfSlits):
        matrix[(i, 0)] = slitProbability

        matrix[(1 + numberOfSlits + (i - 1) * (numberOfTargetsPerSlit - 1), i)] = firstTargetNumber
        matrix[(1 + numberOfSlits + (i - 1) * (numberOfTargetsPerSlit - 1) + numberOfTargetsPerSlit - 1, i)] = lastTargetNumber

        for j in range(
            1 + numberOfSlits + (i - 1) * (numberOfTargetsPerSlit - 1) + 1,
            1 + numberOfSlits + (i - 1) * (numberOfTargetsPerSlit - 1) + numberOfTargetsPerSlit - 1,
        ):
            matrix[(j, i)] = remainingTargetNumber

    for i in range(1 + numberOfSlits, totalNumberOfVertices):
        matrix[(i, i)] = 1

    return matrix


def scalarToZeroFilled(x: complex, shape: tuple[int, ...]) -> np.ndarray[complex]:
    matrix = np.zeros(shape=shape, dtype=complex)
    matrix[(0,) * matrix.ndim] = x
    return matrix


def generateMultislitExperimentMatrixFinal(
    numberOfSlits: int,
    numberOfTargetsPerSlit: int,
) -> tuple[np.ndarray[float], np.ndarray[float]]:
    matrixT = generateMultislitExperimentMatrix(numberOfSlits, numberOfTargetsPerSlit)
    matrix2T = np.matmul(matrixT, matrixT)
    matrix2TAbsSqr = np.abs(matrix2T) ** 2
    bulletsFinalState = np.matmul(
        matrix2TAbsSqr, scalarToZeroFilled(1, (numberOfSlits * numberOfTargetsPerSlit + 2,))
    )
    return (matrix2TAbsSqr, bulletsFinalState)


def main():
    with np.printoptions(precision=3, suppress=True):
        print(*generateMultislitExperimentMatrixFinal(2, 3), sep="\n")
        print(*generateMultislitExperimentMatrixFinal(3, 4), sep="\n")


if __name__ == "__main__":
    main()
