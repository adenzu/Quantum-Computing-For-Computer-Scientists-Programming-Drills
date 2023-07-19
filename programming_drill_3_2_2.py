import numpy as np

# Programming drill 3.2.2

# no parameter for probability of slit to target movement because i dont like it


def generateMultislitExperimentMatrix(
    numberOfSlits: int,
    numberOfTargetsPerSlit: int,
) -> np.ndarray[float]:
    # initial vertex: 1
    # number of slit vertices: numberOfSlits
    # number of target vertices: numberOfSlits * numberOfTargetsPerSlit - numberOfSlits + 1
    totalNumberOfVertices = numberOfSlits * numberOfTargetsPerSlit + 2
    matrix = np.zeros(
        (totalNumberOfVertices, totalNumberOfVertices), dtype=float)

    slitProbability = 1 / numberOfSlits
    targetProbability = 1 / numberOfTargetsPerSlit

    for i in range(1, 1 + numberOfSlits):
        matrix[(i, 0)] = slitProbability

        for j in range(
            1 + numberOfSlits + (i - 1) * (numberOfTargetsPerSlit - 1),
            1 + numberOfSlits +
                (i - 1) * (numberOfTargetsPerSlit - 1) + numberOfTargetsPerSlit
        ):
            matrix[(j, i)] = targetProbability

    for i in range(1 + numberOfSlits, totalNumberOfVertices):
        matrix[(i, i)] = 1

    return matrix


def scalarToZeroFilled(x: float, shape: tuple[int, ...]) -> np.ndarray[float]:
    matrix = np.zeros(shape=shape)
    matrix[(0,) * matrix.ndim] = x
    return matrix


def generateMultislitExperimentMatrixFinal(
    numberOfSlits: int,
    numberOfTargetsPerSlit: int,
) -> tuple[np.ndarray[float], np.ndarray[float]]:
    matrixT = generateMultislitExperimentMatrix(
        numberOfSlits, numberOfTargetsPerSlit)
    matrix2T = np.matmul(matrixT, matrixT)
    bulletsFinalState = np.matmul(
        matrix2T, scalarToZeroFilled(
            1, (numberOfSlits * numberOfTargetsPerSlit + 2,))
    )
    return (matrix2T, bulletsFinalState)


def main():
    with np.printoptions(precision=3, suppress=True):
        print(*generateMultislitExperimentMatrixFinal(2, 3), sep="\n")
        print(*generateMultislitExperimentMatrixFinal(14, 7), sep="\n")


if __name__ == "__main__":
    main()
