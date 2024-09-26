import pyfiglet
import random
import string
import sys
import time
from termcolor import colored
from colorama import Fore, Style, init
from collections import Counter

# Initialize colorama
init(autoreset=True)

# Sample common English words for scoring
COMMON_ENGLISH_WORDS = set([
    "the", "be", "to", "of", "and", "a", "in", "that", "have", "it",
    "I", "you", "he", "she", "we", "they", "not", "this", "but", "by",
    "from", "at", "which", "or", "as", "an", "all", "for", "are", "was",
    "is", "on", "that", "so", "up", "out", "if", "there", "when", "can",
    "more", "other", "some", "what", "like", "no", "just", "see", "him",
    "her", "them", "my", "your", "his", "its", "our", "their", "who",
    "how", "said", "would", "about", "get", "make", "know", "take", "people","Haii",
    "Loosu"
])

def hacker_typing_effect(text, delay=0.01, hackiness=0.01):
    for char in text:
        if char != '\n':
            random_char = random.choice(string.ascii_letters + string.digits)
            sys.stdout.write(colored(random_char, 'green'))
            sys.stdout.flush()
            time.sleep(hackiness)
            sys.stdout.write('\b')
            sys.stdout.flush()
        
        sys.stdout.write(colored(char, 'green'))
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_banner():
    welcome_text = pyfiglet.figlet_format("KRACK")
    hacker_typing_effect(welcome_text, delay=0.005, hackiness=0.005)

def caesar_encrypt(plaintext, shift):
    encrypted = []
    for char in plaintext:
        if char.isalpha():  # Check if the character is an alphabet
            base = ord('A') if char.isupper() else ord('a')
            # Encrypt character and wrap around using modulo
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted.append(encrypted_char)
        else:
            encrypted.append(char)  # Non-alphabetic characters remain unchanged
    return ''.join(encrypted)

def caesar_decrypt(ciphertext, shift):
    decrypted = []
    for char in ciphertext:
        if char.isalpha():  # Check if the character is an alphabet
            base = ord('A') if char.isupper() else ord('a')
            # Decrypt character and wrap around using modulo
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            decrypted.append(decrypted_char)
        else:
            decrypted.append(char)  # Non-alphabetic characters remain unchanged
    return ''.join(decrypted)

def score_text(text):
    words = text.lower().split()
    word_count = Counter(words)
    score = sum(word_count[word] for word in word_count if word in COMMON_ENGLISH_WORDS)
    return score

def brute_force_caesar(ciphertext):
    results = []
    for shift in range(1, 26):  # Check shifts from 1 to 25
        decrypted_text = caesar_decrypt(ciphertext, shift)
        score = score_text(decrypted_text)
        results.append((shift, decrypted_text, score))

    # Sort results based on the score (higher score first)
    results.sort(key=lambda x: (-x[2], x[0]))

    print(Fore.YELLOW + "\nBrute-Force Decryption Results:")
    print(Fore.CYAN + f"{'Shift':<20} {'Decrypted Text'}")
    print(Fore.CYAN + '-' * 60)

    for shift, text, score in results:
        left_shift = (26 - shift) % 26  # Calculate left shift (26 - shift)
        right_shift = shift              # Right shift is the same as shift

        # Create the formatted shift output with arrows
        shift_display = f"← {left_shift}  → {right_shift}"
        print(f"{shift_display:<20} {text}")

def menu():
    print_banner()
    print(Fore.CYAN + """
[1] Caesar Cipher Encode
[2] Caesar Cipher Decode (Brute Force)
[3] Help
[4] About
[5] Exit
""")

def help_menu():
    print(Fore.YELLOW + """
This tool can encode and decode Caesar cipher text.
1. Select [1] to encode a plaintext message.
2. Select [2] to decode a Caesar cipher message by brute-forcing through all possible shifts.
3. The tool will display all decrypted texts for review.
""")

def about_menu():
    print(Fore.YELLOW + """
Caesar Cipher Tool v1.0
Developed by: Aarav
GitHub: https://github.com/aarav-26

This tool is designed to encode and decode messages using the Caesar cipher.
Feel free to contribute or suggest improvements!
""")

def main():
    while True:
        menu()
        choice = input(Fore.MAGENTA + "\nChoose an option: ").strip()
        if choice == '1':
            plaintext = input(Fore.GREEN + "\nEnter the plaintext to encode: ").strip()
            shift = int(input(Fore.GREEN + "Enter the shift value : "))
            encoded_text = caesar_encrypt(plaintext, shift)
            print(Fore.RED + f"\nEncoded Text: {encoded_text}\n")
        elif choice == '2':
            ciphertext = input(Fore.GREEN + "\nEnter the Caesar cipher text to decode: ").strip()
            brute_force_caesar(ciphertext)
        elif choice == '3':
            help_menu()
        elif choice == '4':
            about_menu()
        elif choice == '5':
            print(Fore.GREEN + "\nExiting... Goodbye!")
            break
        else:
            print(Fore.RED + "\nInvalid option! Please choose a valid menu option.\n")

if __name__ == "__main__":
    main()

