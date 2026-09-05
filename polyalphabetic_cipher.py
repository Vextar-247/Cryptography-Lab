text = input("Enter message: ").upper()
key = input("Enter keyword: ").upper()

encrypted = ""
j = 0

# Encryption
for ch in text:
    if ch.isalpha():
        shift = ord(key[j % len(key)]) - ord('A')
        encrypted += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        j += 1
    else:
        encrypted += ch

print("Encrypted Text:", encrypted)

decrypted = ""
j = 0

# Decryption
for ch in encrypted:
    if ch.isalpha():
        shift = ord(key[j % len(key)]) - ord('A')
        decrypted += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
        j += 1
    else:
        decrypted += ch

print("Decrypted Text:", decrypted)