def encrypt(plaintext, key):
    """
    Encrypts plaintext using the Caesar Cipher algorithm with the given key
    """
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift = ord(char.lower()) - ord('a')
            new_char = chr((shift + key) % 26 + ord('a'))
            ciphertext += new_char.upper() if char.isupper() else new_char
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, key):
    """
    Decrypts ciphertext using the Caesar Cipher algorithm with the given key
    """
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift = ord(char.lower()) - ord('a')
            new_char = chr((shift - key) % 26 + ord('a'))
            plaintext += new_char.upper() if char.isupper() else new_char
        else:
            plaintext += char
    return plaintext

# Example usage
plaintext = " "
key = 30
ciphertext = encrypt(plaintext, key)
print(ciphertext)
decrypted_plaintext = decrypt(ciphertext, key)
print(decrypted_plaintext)