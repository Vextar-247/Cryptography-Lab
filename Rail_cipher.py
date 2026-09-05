def encrypt(text, key):
    rail = ['' for _ in range(key)]
    row = 0
    direction = 1

    for ch in text:
        rail[row] += ch

        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        row += direction

    return ''.join(rail)


def decrypt(cipher, key):
    n = len(cipher)

    pattern = [[False] * n for _ in range(key)]

    row = 0
    direction = 1

    for col in range(n):
        pattern[row][col] = True

        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        row += direction

    index = 0
    rail = [[''] * n for _ in range(key)]

    for i in range(key):
        for j in range(n):
            if pattern[i][j]:
                rail[i][j] = cipher[index]
                index += 1

    result = ""
    row = 0
    direction = 1

    for col in range(n):
        result += rail[row][col]

        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        row += direction

    return result


text = input("Enter message: ")
key = int(input("Enter number of rails: "))

encrypted = encrypt(text, key)
print("Encrypted Text:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted Text:", decrypted)