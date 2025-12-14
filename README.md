# 4 Types of Cryptographic & System Attacks

This repository demonstrates the implementation of four common types of attacks in cybersecurity. These scripts are for educational purposes to understand vulnerabilities and how to mitigate them.

## 📂 Project Structure

- `brute_force_caesar.py` - Brute-force attack on Caesar Cipher.
- `dictionary_attack.py` - Dictionary attack on weak password hashes (MD5).
- `frequency_attack.py` - Frequency analysis on substitution ciphers.
- `padding_oracle_attack.py` - Simulation of a Padding Oracle Attack on AES-CBC.

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3 installed. You will also need the `cryptography` library for the Padding Oracle attack.

```bash
pip install cryptography
```

### 1. Brute-force Attack (Caesar Cipher)
Attempts to decrypt a Caesar Cipher encrypted message by trying all possible 26 shifts.

**Usage:**
```bash
python brute_force_caesar.py
```
**Output:** It prints the result of all 26 possible shifts, allowing the user to identify the readable plaintext.

### 2. Dictionary Attack
Cracks a password by comparing its hash against a list of common passwords (dictionary). This script uses MD5 for demonstration.

**Usage:**
```bash
python dictionary_attack.py
```
**Output:** If the target hash matches a word in the dictionary, it reveals the password.

### 3. Frequency Analysis
Analyzes the frequency of letters in a ciphertext. This is effective against simple substitution ciphers where letters map one-to-one.

**Usage:**
```bash
python frequency_attack.py
```
**Output:** Displays the count of each character in the ciphertext, useful for statistical analysis.

### 4. Padding Oracle Attack
Simulates a Padding Oracle vulnerability in AES-CBC mode. It checks if the padding of a decrypted message is valid, which can be exploited to decrypt the message byte-by-byte.

**Usage:**
```bash
python padding_oracle_attack.py
```
**Output:** It attempts to modify the last byte of the ciphertext and checks if the oracle returns "Valid padding".

## ⚠️ Disclaimer
These scripts are intended **only for educational and research purposes**. Do not use them on systems you do not own or have explicit permission to test.
