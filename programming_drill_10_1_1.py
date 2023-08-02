import numpy as np
import matplotlib.pyplot as plt


def computeShannonEntropy(ps: list[float]) -> float:
    def item(p):
        if p == 0:
            return 0
        else:
            return -p * np.log2(p)
    return sum(item(p) for p in ps)


def visualizeProbabilityDistribution(ps: list[float]):
    # make it so vertical axis upper boundary is 1.0
    plt.ylim(0, 1.0)
    # make x axis have letters instead of indices
    plt.xticks(range(len(ps)), [chr(ord('A') + i) for i in range(len(ps))])
    plt.bar(range(len(ps)), ps)
    plt.show()


def main():
    while True:
        letterCount = int(input('Please enter the number of letters: '))
        probabilityDistribution = []
        for i in range(letterCount):
            probabilityDistribution.append(
                float(input(f'Please enter the probability of letter {i + 1}: ')))
        print(
            f'The Shannon entropy of the probability distribution is {computeShannonEntropy(probabilityDistribution)}.')
        visualizeProbabilityDistribution(probabilityDistribution)
        if input('Do you want to continue? (y/n) ').lower() != 'y':
            break


if __name__ == '__main__':
    main()
