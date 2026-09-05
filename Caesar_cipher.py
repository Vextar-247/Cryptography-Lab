text = input("Enter message: ")
shift = int(input("Enter shift value: "))

# Encryption
encrypted = ""
for ch in text:
    if ch.isalpha():
        base = ord('A') if ch.isupper() else ord('a')
        encrypted += chr((ord(ch) - base + shift) % 26 + base)
    else:
        encrypted += ch

print("Encrypted Text:", encrypted)

# Decryption
decrypted = ""
for ch in encrypted:
    if ch.isalpha():
        base = ord('A') if ch.isupper() else ord('a')
        decrypted += chr((ord(ch) - base - shift) % 26 + base)
    else:
        decrypted += ch

print("Decrypted Text:", decrypted)