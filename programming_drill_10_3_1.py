import itertools


def indicesToSequence(indices: list[int], sequenceLength: int, putOne: bool = True) -> tuple[int, ...]:
    result = [0 if putOne else 1] * sequenceLength
    for i in indices:
        result[i] = 1 if putOne else 0
    return tuple(result)


def generateAllTypicalSequences(probabilityOfZero: float, sequenceLength: int) -> list[int]:
    numberOfZeros = int(sequenceLength * probabilityOfZero)
    numberOfOnes = sequenceLength - numberOfZeros

    putNumber = 0 if numberOfZeros < numberOfOnes else 1
    numberOfIndices = min(numberOfZeros, numberOfOnes)

    result = [()]
    for i in range(numberOfIndices):
        news = []
        for j in range(i, sequenceLength):
            news.append(j)
        result = [(*a, b) for a in result for b in news]
        result = list(filter(lambda x: sum(x.count(i)
                      for i in x) == len(x), result))
        result = set(tuple(sorted(a)) for a in result)

    return sorted(indicesToSequence(a, sequenceLength, putNumber) for a in result)


def generateAllTypicalSequences2(probabilityOfZero: float, sequenceLength: int) -> list[int]:
    return sorted(indicesToSequence(a, sequenceLength, 0) for a in itertools.combinations(range(sequenceLength), int(sequenceLength * probabilityOfZero)))


def main():
    probabilityOfZero = 0.5
    sequenceLength = 4

    print(generateAllTypicalSequences(probabilityOfZero, sequenceLength))
    print(generateAllTypicalSequences2(probabilityOfZero, sequenceLength))

    # test performance
    import timeit
    print(timeit.timeit(lambda: generateAllTypicalSequences(
        probabilityOfZero, sequenceLength), number=1000))
    print(timeit.timeit(lambda: generateAllTypicalSequences2(
        probabilityOfZero, sequenceLength), number=1000))


if __name__ == '__main__':
    main()
