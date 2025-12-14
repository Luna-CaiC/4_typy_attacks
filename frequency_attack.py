# Frequency Analysis on Substitution Cipher

from collections import Counter
import string

def frequency_analysis(ciphertext):
    counter = Counter(filter(str.isalpha, ciphertext.upper()))
    sorted_letters = sorted(counter.items(), key=lambda item: item[1], reverse=True)
    print("🔍 Letter Frequencies in Ciphertext:")
    for letter, count in sorted_letters:
        print(f"{letter}: {count}")

if __name__ == "__main__":
    ciphertext = "JUST HAHA HEYHEY"
    print(f"Ciphertext: {ciphertext}")
    frequency_analysis(ciphertext)
