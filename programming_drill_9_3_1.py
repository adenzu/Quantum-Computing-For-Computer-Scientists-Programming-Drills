import numpy as np


def byteToBits(byte: np.uint8) -> np.ndarray[np.uint8]:
    return np.array([byte >> i & 1 for i in range(8)], dtype=np.uint8)


def alice92(size: int) -> np.ndarray[np.uint8]:
    return np.random.randint(0, 256, size, dtype=np.uint8)


def bob92(size: int) -> np.ndarray[np.uint8]:
    return np.random.randint(0, 256, size, dtype=np.uint8)


def knuth92(bitSent: np.ndarray[np.uint8], receivingBasis: np.ndarray[np.uint8]) -> tuple[np.ndarray[np.uint8], float]:
    agreedBits = []
    for sentByte, receivingBasisByte in zip(bitSent, receivingBasis):
        sentBits = byteToBits(sentByte)
        receivingBasisBits = byteToBits(receivingBasisByte)
        for sentBit, receivingBasisBit in zip(sentBits, receivingBasisBits):
            if receivingBasisBit == 0 and sentBit == 1 and np.random.randint(0, 2) == 0:
                agreedBits.append(1)
            elif receivingBasisBit == 1 and sentBit == 0 and np.random.randint(0, 2) == 0:
                agreedBits.append(0)
    accuracy = len(agreedBits) / (len(bitSent) * 8)
    return (np.array(agreedBits, dtype=np.uint8), accuracy)


def main():
    size = 1024
    bitSent = alice92(size)
    receivingBasis = bob92(size)
    agreedBits, accuracy = knuth92(bitSent, receivingBasis)
    print('Bit sent: ' + str(bitSent))
    print('Receiving basis: ' + str(receivingBasis))
    print('Agreed bits: ' + str(agreedBits))
    print('Accuracy: ' + str(accuracy))


if __name__ == '__main__':
    main()
