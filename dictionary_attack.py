#  Dictionary Attack on Weak Password Hashes

import hashlib

common_passwords = ["password", "123abc", "hello88", "123456", "admin"]
stored_hash = hashlib.md5("hello88".encode()).hexdigest()

def dictionary_attack(target_hash, wordlist):
    for word in wordlist:
        if hashlib.md5(word.encode()).hexdigest() == target_hash:
            print(f"🔓 Cracked password: {word}")
            return word
    print("❌ No match found.")
    return None

if __name__ == "__main__":
    print(f"Stored MD5 Hash: {stored_hash}")
    dictionary_attack(stored_hash, common_passwords)
