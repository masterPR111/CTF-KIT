"""
Cipher Tools Module
"""
import re
from config import Colors as C, FLAG_PATTERNS


def caesar_bruteforce(text):
    results = []
    for shift in range(26):
        result = ""
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base - shift) % 26 + base)
            else:
                result += char
        results.append((shift, result))
    return results


def caesar_shift(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def xor_bruteforce(text):
    try:
        data = bytes.fromhex(text)
    except:
        data = text.encode()
    
    results = []
    for key in range(256):
        result = bytes([b ^ key for b in data])
        try:
            decoded = result.decode('utf-8')
            if all(32 <= ord(c) < 127 for c in decoded):
                results.append((key, decoded))
        except:
            pass
    return results


def xor_with_key(text, key):
    try:
        data = bytes.fromhex(text)
    except:
        data = text.encode()
    result = bytes([b ^ key for b in data])
    return result.decode('utf-8', errors='ignore')


def vigenere_decrypt(text, key):
    result = ""
    key_idx = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_idx % len(key)].lower()) - ord('a')
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
            key_idx += 1
        else:
            result += char
    return result


def vigenere_encrypt(text, key):
    result = ""
    key_idx = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_idx % len(key)].lower()) - ord('a')
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
            key_idx += 1
        else:
            result += char
    return result


def atbash(text):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr(ord('Z') - (ord(char) - ord('A')))
            else:
                result += chr(ord('z') - (ord(char) - ord('a')))
        else:
            result += char
    return result


def find_flags(text):
    found = []
    for pattern in FLAG_PATTERNS:
        for match in re.findall(pattern, text, re.IGNORECASE):
            found.append(match)
    return found


def run():
    while True:
        print(f"""{C.CYAN}{C.BOLD}
    ╔═══════════════════════════════════════════╗
    ║           CIPHER TOOLS                    ║
    ╠═══════════════════════════════════════════╣
    ║  {C.WHITE}[1]{C.CYAN}  Caesar Brute-force                  ║
    ║  {C.WHITE}[2]{C.CYAN}  Caesar with Shift                    ║
    ║  {C.WHITE}[3]{C.CYAN}  XOR Brute-force                      ║
    ║  {C.WHITE}[4]{C.CYAN}  XOR with Key                        ║
    ║  {C.WHITE}[5]{C.CYAN}  String Reverse                      ║
    ║  {C.WHITE}[6]{C.CYAN}  Vigenère Decrypt                    ║
    ║  {C.WHITE}[7]{C.CYAN}  Vigenère Encrypt                    ║
    ║  {C.WHITE}[8]{C.CYAN}  Atbash Cipher                       ║
    ║  {C.WHITE}[9]{C.CYAN}  Flag Search                         ║
    ║  {C.WHITE}[0]{C.CYAN}  Back                                ║
    ╚═══════════════════════════════════════════╝
        {C.RESET}""")

        choice = input(f"{C.MAGENTA}[?]{C.RESET} Select option: ").strip()

        if choice == "0":
            return
        elif choice == "1":
            text = input(f"{C.MAGENTA}[?]{C.RESET} Ciphertext: ")
            for shift, result in caesar_bruteforce(text):
                print(f"  {C.YELLOW}Shift {shift:2d}{C.RESET}: {result}")
        elif choice == "2":
            text = input(f"{C.MAGENTA}[?]{C.RESET} Text: ")
            shift = int(input(f"{C.MAGENTA}[?]{C.RESET} Shift: "))
            print(f"{C.GREEN}[+]{C.RESET} {caesar_shift(text, shift)}")
        elif choice == "3":
            text = input(f"{C.MAGENTA}[?]{C.RESET} Hex or text: ")
            for key, result in xor_bruteforce(text):
                print(f"  {C.YELLOW}Key {key:3d}{C.RESET}: {result}")
        elif choice == "4":
            text = input(f"{C.MAGENTA}[?]{C.RESET} Hex or text: ")
            key = int(input(f"{C.MAGENTA}[?]{C.RESET} Key (0-255): "))
            print(f"{C.GREEN}[+]{C.RESET} {xor_with_key(text, key)}")
        elif choice == "5":
            text = input(f"{C.MAGENTA}[?]{C.RESET} Text: ")
            print(f"{C.GREEN}[+]{C.RESET} {text[::-1]}")
        elif choice == "6":
            text = input(f"{C.MAGENTA}[?]{C.RESET} Text: ")
            key = input(f"{C.MAGENTA}[?]{C.RESET} Key: ")
            print(f"{C.GREEN}[+]{C.RESET} {vigenere_decrypt(text, key)}")
        elif choice == "7":
            text = input(f"{C.MAGENTA}[?]{C.RESET} Text: ")
            key = input(f"{C.MAGENTA}[?]{C.RESET} Key: ")
            print(f"{C.GREEN}[+]{C.RESET} {vigenere_encrypt(text, key)}")
        elif choice == "8":
            text = input(f"{C.MAGENTA}[?]{C.RESET} Text: ")
            print(f"{C.GREEN}[+]{C.RESET} {atbash(text)}")
        elif choice == "9":
            text = input(f"{C.MAGENTA}[?]{C.RESET} Text: ")
            flags = find_flags(text)
            if flags:
                for flag in flags:
                    print(f"  {C.GREEN}🚩 {flag}{C.RESET}")
            else:
                print(f"{C.YELLOW}[!]{C.RESET} No flags found")
        else:
            print(f"{C.RED}[-]{C.RESET} Invalid option")

        input(f"\n{C.DIM}Press Enter...{C.RESET}")
