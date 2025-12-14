# Padding Oracle Attack on AES-CBC

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

key = os.urandom(16)
iv = os.urandom(16)

def encrypt(plaintext):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    padder = padding.PKCS7(128).padder()
    padded = padder.update(plaintext.encode()) + padder.finalize()
    encryptor = cipher.encryptor()
    return encryptor.update(padded) + encryptor.finalize()

def padding_oracle(ciphertext):
    try:
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()
        
        # 必须尝试去填充（Unpad）才能验证 Padding 是否正确
        unpadder = padding.PKCS7(128).unpadder()
        unpadder.update(decrypted_padded) + unpadder.finalize()
        return True
    except Exception:
        return False

if __name__ == "__main__":
    msg = "A Secret Message!"
    ct = encrypt(msg)
    print(f"🔒 Encrypted: {ct.hex()}")

    print("\n🔍 Simulating Padding Oracle:")
    for i in range(256):
        fake_ct = ct[:-1] + bytes([i])
        if padding_oracle(fake_ct):
            print(f"✅ Valid padding for last byte: {i}")
            break
