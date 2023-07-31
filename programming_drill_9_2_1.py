import numpy as np


def byteToBits(byte: np.uint8) -> np.ndarray[np.uint8]:
    return np.array([byte >> i & 1 for i in range(8)], dtype=np.uint8)


def alice(size: int) -> tuple[np.ndarray[np.uint8], np.ndarray[np.uint8]]:
    return (np.random.randint(0, 256, size, dtype=np.uint8), np.random.randint(0, 256, size, dtype=np.uint8))


def bob(size: int) -> np.ndarray[np.uint8]:
    return np.random.randint(0, 256, size, dtype=np.uint8)


def knuth(bitSent: np.ndarray[np.uint8], sendingBasis: np.ndarray[np.uint8], receivingBasis: np.ndarray[np.uint8]) -> tuple[np.ndarray[np.uint8], float]:
    randomBytes = np.random.randint(
        0, 256, len(bitSent), dtype=np.uint8)
    bitReceived = np.array([(randomByte & (sendingBasisByte ^ receivingBasisByte)) | (receivedByte & ~(sendingBasisByte ^ receivingBasisByte))
                            for randomByte, receivedByte, sendingBasisByte, receivingBasisByte in zip(randomBytes, bitSent, sendingBasis, receivingBasis)], dtype=np.uint8)
    equalBits = np.array([byteToBits(byte)
                         for byte in ~(bitSent ^ bitReceived)])
    accuracy = np.sum(equalBits) / (len(bitSent) * 8)
    return (bitReceived, accuracy)


def main():
    size = 1024
    bitSent, sendingBasis = alice(size)
    receivingBasis = bob(size)
    bitReceived, accuracy = knuth(bitSent, sendingBasis, receivingBasis)
    print('Bit sent: ' + str(bitSent))
    print('Sending basis: ' + str(sendingBasis))
    print('Receiving basis: ' + str(receivingBasis))
    print('Bit received: ' + str(bitReceived))
    print('Accuracy: ' + str(accuracy))


if __name__ == '__main__':
    main()
