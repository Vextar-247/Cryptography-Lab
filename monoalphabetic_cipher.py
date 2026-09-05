alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "QWERTYUIOPASDFGHJKLZXCVBNM"

text = input("Enter message: ").upper()

# Encryption
encrypted = ""
for ch in text:
    if ch in alphabet:
        encrypted += key[alphabet.index(ch)]
    else:
        encrypted += ch

print("Encrypted Text:", encrypted)

# Decryption
decrypted = ""
for ch in encrypted:
    if ch in key:
        decrypted += alphabet[key.index(ch)]
    else:
        decrypted += ch

print("Decrypted Text:", decrypted)