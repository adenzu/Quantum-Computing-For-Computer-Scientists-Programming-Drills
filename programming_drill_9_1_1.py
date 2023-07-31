
# programming drill 9.1.1

def positiveModulo(n: int, m: int) -> int:
    return (n % m + m) % m


def encryptCaesar(plaintext: str) -> str:
    correspondingLetters = {'a': 'h', 'b': 'i', 'c': 'j', 'd': 'k', 'e': 'l', 'f': 'm', 'g': 'n', 'h': 'o', 'i': 'p', 'j': 'q', 'k': 'r', 'l': 's',
                            'm': 't', 'n': 'u', 'o': 'v', 'p': 'w', 'q': 'x', 'r': 'y', 's': 'z', 't': 'a', 'u': 'b', 'v': 'c', 'w': 'd', 'x': 'e', 'y': 'f', 'z': 'g', 'A': 'H', 'B': 'I', 'C': 'J', 'D': 'K', 'E': 'L', 'F': 'M', 'G': 'N', 'H': 'O', 'I': 'P', 'J': 'Q', 'K': 'R', 'L': 'S', 'M': 'T', 'N': 'U', 'O': 'V', 'P': 'W', 'Q': 'X', 'R': 'Y', 'S': 'Z', 'T': 'A', 'U': 'B', 'V': 'C', 'W': 'D', 'X': 'E', 'Y': 'F', 'Z': 'G'}
    return ''.join(correspondingLetters[letter] if letter in correspondingLetters else letter for letter in plaintext)


def decryptCaesar(ciphertext: str) -> str:
    correspondingLetters = {'h': 'a', 'i': 'b', 'j': 'c', 'k': 'd', 'l': 'e', 'm': 'f', 'n': 'g', 'o': 'h', 'p': 'i', 'q': 'j', 'r': 'k', 's': 'l',
                            't': 'm', 'u': 'n', 'v': 'o', 'w': 'p', 'x': 'q', 'y': 'r', 'z': 's', 'a': 't', 'b': 'u', 'c': 'v', 'd': 'w', 'e': 'x', 'f': 'y', 'g': 'z', 'H': 'A', 'I': 'B', 'J': 'C', 'K': 'D', 'L': 'E', 'M': 'F', 'N': 'G', 'O': 'H', 'P': 'I', 'Q': 'J', 'R': 'K', 'S': 'L', 'T': 'M', 'U': 'N', 'V': 'O', 'W': 'P', 'X': 'Q', 'Y': 'R', 'Z': 'S', 'A': 'T', 'B': 'U', 'C': 'V', 'D': 'W', 'E': 'X', 'F': 'Y', 'G': 'Z'}
    return ''.join(correspondingLetters[letter] if letter in correspondingLetters else letter for letter in ciphertext)


def main():
    testTexts = ['hello', 'world', 'hello world', 'HELLO WORLD']
    for text in testTexts:
        ciphertext = encryptCaesar(text)
        print('Ciphertext: ' + ciphertext)
        print('Decrypted: ' + decryptCaesar(ciphertext))


if __name__ == '__main__':
    main()
