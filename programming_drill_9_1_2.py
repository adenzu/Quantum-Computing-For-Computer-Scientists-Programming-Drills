
def oneTimePadEncryptAndDecrypt(byteArray: bytes, key: bytes) -> bytes:
    if len(key) > 1:
        raise ValueError('Key must be one byte long')
    key = key[0]
    return bytes(byte ^ key for byte in byteArray)


def main():
    plainTexts = [b'hello', b'world', b'hello world', b'HELLO WORLD']
    for text in plainTexts:
        ciphertext = oneTimePadEncryptAndDecrypt(text, b'x')
        print('Ciphertext: ' + str(ciphertext))
        print('Decrypted: ' + str(oneTimePadEncryptAndDecrypt(ciphertext, b'x')))


if __name__ == '__main__':
    main()
