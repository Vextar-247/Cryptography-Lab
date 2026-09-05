import math

def get_order(key):
    return sorted(range(len(key)), key=lambda k: key[k])


def encrypt(text, key):
    text = text.replace(" ", "").upper()

    while len(text) % len(key) != 0:
        text += "X"

    rows = len(text) // len(key)
    matrix = []

    index = 0
    for i in range(rows):
        matrix.append(list(text[index:index + len(key)]))
        index += len(key)

    order = get_order(key)

    cipher = ""
    for col in order:
        for row in matrix:
            cipher += row[col]

    return cipher


def decrypt(cipher, key):
    rows = len(cipher) // len(key)
    order = get_order(key)

    matrix = [[''] * len(key) for _ in range(rows)]

    index = 0
    for col in order:
        for row in range(rows):
            matrix[row][col] = cipher[index]
            index += 1

    text = ""
    for row in matrix:
        text += "".join(row)

    return text.rstrip("X")


message = input("Enter message: ")
key = input("Enter key: ").upper()

first = encrypt(message, key)
second = encrypt(first, key)

print("Encrypted Text:", second)

first_dec = decrypt(second, key)
original = decrypt(first_dec, key)

print("Decrypted Text:", original)