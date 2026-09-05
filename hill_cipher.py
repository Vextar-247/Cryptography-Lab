key = [[3, 3], [2, 5]]
inverse = [[15, 17], [20, 9]]

text = input("Enter message: ").upper().replace(" ", "")

if len(text) % 2 != 0:
    text += "X"

def process(msg, matrix):
    result = ""
    for i in range(0, len(msg), 2):
        a = ord(msg[i]) - 65
        b = ord(msg[i + 1]) - 65

        x = (matrix[0][0] * a + matrix[0][1] * b) % 26
        y = (matrix[1][0] * a + matrix[1][1] * b) % 26

        result += chr(x + 65)
        result += chr(y + 65)
    return result

encrypted = process(text, key)
print("Encrypted Text:", encrypted)

decrypted = process(encrypted, inverse)
print("Decrypted Text:", decrypted)