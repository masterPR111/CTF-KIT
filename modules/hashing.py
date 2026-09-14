"""
Hashing Module
"""
import hashlib
from config import Colors as C


def hash_text(text, algo):
    h = hashlib.new(algo)
    h.update(text.encode())
    return h.hexdigest()


def hash_file(filepath):
    with open(filepath, 'rb') as f:
        data = f.read()
    results = {}
    for algo in ['md5', 'sha1', 'sha256', 'sha512']:
        h = hashlib.new(algo)
        h.update(data)
        results[algo] = h.hexdigest()
    return results


def identify_hash(hash_str):
    hash_str = hash_str.strip()
    length = len(hash_str)
    
    if not all(c in '0123456789abcdefABCDEF' for c in hash_str):
        return "Unknown (not hex)"
    
    types = {
        32: "MD5, MD4, NTLM, LM",
        40: "SHA1, MySQL5, RIPEMD-160",
        56: "SHA224",
        64: "SHA256, SHA3-256, BLAKE2s",
        96: "SHA384, SHA3-384",
        128: "SHA512, SHA3-512, BLAKE2b, Whirlpool",
    }
    
    return types.get(length, f"Unknown (length: {length})")


def run():
    while True:
        print(f"""{C.CYAN}{C.BOLD}
    ╔═══════════════════════════════════════════╗
    ║              HASHING                      ║
    ╠═══════════════════════════════════════════╣
    ║  {C.WHITE}[1]{C.CYAN}  MD5                                  ║
    ║  {C.WHITE}[2]{C.CYAN}  SHA1                                 ║
    ║  {C.WHITE}[3]{C.CYAN}  SHA256                               ║
    ║  {C.WHITE}[4]{C.CYAN}  SHA512                               ║
    ║  {C.WHITE}[5]{C.CYAN}  All Hashes                           ║
    ║  {C.WHITE}[6]{C.CYAN}  Hash a File                          ║
    ║  {C.WHITE}[7]{C.CYAN}  Identify Hash Type                   ║
    ║  {C.WHITE}[0]{C.CYAN}  Back                                 ║
    ╚═══════════════════════════════════════════╝
        {C.RESET}""")

        choice = input(f"{C.MAGENTA}[?]{C.RESET} Select option: ").strip()

        if choice == "0":
            return
        elif choice in ["1", "2", "3", "4"]:
            text = input(f"{C.MAGENTA}[?]{C.RESET} Text: ")
            algo = {"1": "md5", "2": "sha1", "3": "sha256", "4": "sha512"}[choice]
            print(f"{C.GREEN}[+]{C.RESET} {algo.upper()}: {hash_text(text, algo)}")
        elif choice == "5":
            text = input(f"{C.MAGENTA}[?]{C.RESET} Text: ")
            for algo in ['md5', 'sha1', 'sha256', 'sha512']:
                print(f"  {C.YELLOW}{algo.upper():8}{C.RESET} {hash_text(text, algo)}")
        elif choice == "6":
            filepath = input(f"{C.MAGENTA}[?]{C.RESET} File path: ")
            try:
                results = hash_file(filepath)
                for algo, h in results.items():
                    print(f"  {C.YELLOW}{algo.upper():8}{C.RESET} {h}")
            except Exception as e:
                print(f"{C.RED}[-]{C.RESET} {e}")
        elif choice == "7":
            hash_str = input(f"{C.MAGENTA}[?]{C.RESET} Hash: ")
            print(f"{C.GREEN}[+]{C.RESET} Possible types: {identify_hash(hash_str)}")
        else:
            print(f"{C.RED}[-]{C.RESET} Invalid option")

        input(f"\n{C.DIM}Press Enter...{C.RESET}")
