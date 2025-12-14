# Brute-force Attack on Caesar Cipher

def caesar_encrypt(plaintext, shift):
    result = ""
    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

def brute_force_attack(ciphertext):
    print("🔍 Brute-force Decryption Attempts:")
    for shift in range(26):
        print(f"Shift {shift}: {caesar_decrypt(ciphertext, shift)}")

if __name__ == "__main__":
    text = "Brute Force on Caesar"
    encrypted = caesar_encrypt(text, 3)
    print(f"🔒 Encrypted: {encrypted}")
    brute_force_attack(encrypted)
