"""
Encoding/Decoding Module - Beautiful UI
"""
import base64
import binascii
import codecs
import urllib.parse
from ui import (
    C, show_banner, ask, pause, print_success, print_error,
    print_section, print_table, clear
)


MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
}
MORSE_REVERSE = {v: k for k, v in MORSE_CODE.items()}


def run():
    """Interactive menu"""
    while True:
        clear()
        show_banner()
        
        # Menu
        options = [
            ("1", "📝", "Base64 Encode"),
            ("2", "📝", "Base64 Decode"),
            ("3", "🔢", "Hex Encode"),
            ("4", "🔢", "Hex Decode"),
            ("5", "🔗", "URL Encode"),
            ("6", "🔗", "URL Decode"),
            ("7", "🔄", "ROT13"),
            ("8", "💻", "Binary Encode"),
            ("9", "💻", "Binary Decode"),
            ("10", "🔤", "ASCII to Char"),
            ("11", "🔤", "Char to ASCII"),
            ("12", "📡", "Morse Encode"),
            ("13", "📡", "Morse Decode"),
            ("14", "🔍", "Auto-detect & Decode"),
            ("0", "⬅️ ", "Back"),
        ]
        
        print(f"  {C.BCYAN}{C.BOLD}╭─ 🔐 Encoding / Decoding ─────────────────╮{C.RESET}")
        for key, icon, label in options:
            print(f"  {C.BCYAN}│{C.RESET} {C.BCYAN}{C.BOLD}[{key:>2}]{C.RESET} {icon}  {C.WHITE}{label}{C.RESET}")
        print(f"  {C.BCYAN}{C.BOLD}╰──────────────────────────────────────────╯{C.RESET}")
        print()
        
        choice = ask("Select option")
        
        if choice == "0":
            return
        
        try:
            if choice == "1":
                text = ask("Text")
                print_success(base64.b64encode(text.encode()).decode())
            elif choice == "2":
                text = ask("Base64")
                print_success(base64.b64decode(text).decode('utf-8', errors='ignore'))
            elif choice == "3":
                text = ask("Text")
                print_success(text.encode().hex())
            elif choice == "4":
                text = ask("Hex")
                print_success(binascii.unhexlify(text).decode('utf-8', errors='ignore'))
            elif choice == "5":
                text = ask("Text")
                print_success(urllib.parse.quote(text))
            elif choice == "6":
                text = ask("URL")
                print_success(urllib.parse.unquote(text))
            elif choice == "7":
                text = ask("Text")
                print_success(codecs.encode(text, 'rot_13'))
            elif choice == "8":
                text = ask("Text")
                print_success(' '.join(format(ord(c), '08b') for c in text))
            elif choice == "9":
                text = ask("Binary")
                print_success(''.join(chr(int(b, 2)) for b in text.split()))
            elif choice == "10":
                text = ask("ASCII codes")
                print_success(''.join(chr(int(c)) for c in text.split()))
            elif choice == "11":
                text = ask("Text")
                print_success(' '.join(str(ord(c)) for c in text))
            elif choice == "12":
                text = ask("Text")
                print_success(' '.join(MORSE_CODE.get(c.upper(), c) for c in text))
            elif choice == "13":
                text = ask("Morse (space separated)")
                print_success(''.join(MORSE_REVERSE.get(m, m) for m in text.split()))
            elif choice == "14":
                text = ask("Text")
                print_section("Auto Decode Results")
                results = []
                
                try:
                    decoded = base64.b64decode(text).decode('utf-8', errors='ignore')
                    if decoded.isprintable():
                        results.append(("Base64", decoded))
                except: pass
                
                try:
                    decoded = binascii.unhexlify(text).decode('utf-8', errors='ignore')
                    if decoded.isprintable():
                        results.append(("Hex", decoded))
                except: pass
                
                decoded = urllib.parse.unquote(text)
                if decoded != text:
                    results.append(("URL", decoded))
                
                decoded = codecs.encode(text, 'rot_13')
                if decoded != text:
                    results.append(("ROT13", decoded))
                
                if results:
                    for name, result in results:
                        print(f"  {C.BYELLOW}{name:10}{C.RESET} {C.GREEN}{result}{C.RESET}")
                else:
                    print_warning("No decodings found")
            else:
                print_error("Invalid option")
        except Exception as e:
            print_error(str(e))
        
        pause()
