"""
Crypto Attacks Module
"""
from collections import Counter
from config import Colors as C


def frequency_analysis(text):
    letters = [c.lower() for c in text if c.isalpha()]
    total = len(letters)
    if total == 0:
        return {}
    counter = Counter(letters)
    return {letter: (count / total) * 100 for letter, count in counter.most_common()}


def rsa_small_e(n, e, c):
    try:
        m = round(c ** (1 / e))
        for i in range(-100, 100):
            candidate = m + i
            if pow(candidate, e, n) == c:
                return candidate
    except:
        pass
    return None


def rsa_common_modulus(n, e1, c1, e2, c2):
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        g, x, y = egcd(b % a, a)
        return g, y - (b // a) * x, x
    
    g, a, b = egcd(e1, e2)
    if g != 1:
        return None
    
    if a < 0:
        c1 = pow(c1, -1, n)
        a = -a
    if b < 0:
        c2 = pow(c2, -1, n)
        b = -b
    
    return (pow(c1, a, n) * pow(c2, b, n)) % n


def run():
    while True:
        print(f"""{C.CYAN}{C.BOLD}
    ╔═══════════════════════════════════════════╗
    ║            CRYPTO ATTACKS                 ║
    ╠═══════════════════════════════════════════╣
    ║  {C.WHITE}[1]{C.CYAN}  Frequency Analysis                  ║
    ║  {C.WHITE}[2]{C.CYAN}  RSA Small e Attack                  ║
    ║  {C.WHITE}[3]{C.CYAN}  RSA Common Modulus                  ║
    ║  {C.WHITE}[4]{C.CYAN}  Prime Factorization                 ║
    ║  {C.WHITE}[0]{C.CYAN}  Back                                ║
    ╚═══════════════════════════════════════════╝
        {C.RESET}""")

        choice = input(f"{C.MAGENTA}[?]{C.RESET} Select option: ").strip()

        if choice == "0":
            return
        elif choice == "1":
            text = input(f"{C.MAGENTA}[?]{C.RESET} Text: ")
            freq = frequency_analysis(text)
            for letter, pct in list(freq.items())[:15]:
                bar = '█' * int(pct)
                print(f"  {C.YELLOW}{letter.upper()}{C.RESET}: {pct:5.2f}% {bar}")
        elif choice == "2":
            n = int(input(f"{C.MAGENTA}[?]{C.RESET} n: "))
            e = int(input(f"{C.MAGENTA}[?]{C.RESET} e: "))
            c = int(input(f"{C.MAGENTA}[?]{C.RESET} c: "))
            result = rsa_small_e(n, e, c)
            if result:
                try:
                    print(f"{C.GREEN}[+]{C.RESET} {bytes.fromhex(hex(result)[2:]).decode()}")
                except:
                    print(f"{C.GREEN}[+]{C.RESET} {result}")
            else:
                print(f"{C.RED}[-]{C.RESET} Attack failed")
        elif choice == "3":
            n = int(input(f"{C.MAGENTA}[?]{C.RESET} n: "))
            e1 = int(input(f"{C.MAGENTA}[?]{C.RESET} e1: "))
            c1 = int(input(f"{C.MAGENTA}[?]{C.RESET} c1: "))
            e2 = int(input(f"{C.MAGENTA}[?]{C.RESET} e2: "))
            c2 = int(input(f"{C.MAGENTA}[?]{C.RESET} c2: "))
            result = rsa_common_modulus(n, e1, c1, e2, c2)
            if result:
                try:
                    print(f"{C.GREEN}[+]{C.RESET} {bytes.fromhex(hex(result)[2:]).decode()}")
                except:
                    print(f"{C.GREEN}[+]{C.RESET} {result}")
            else:
                print(f"{C.RED}[-]{C.RESET} Attack failed")
        elif choice == "4":
            n = int(input(f"{C.MAGENTA}[?]{C.RESET} n: "))
            factors = []
            d = 2
            while d * d <= n:
                while n % d == 0:
                    factors.append(d)
                    n //= d
                d += 1
            if n > 1:
                factors.append(n)
            print(f"{C.GREEN}[+]{C.RESET} Factors: {factors}")
        else:
            print(f"{C.RED}[-]{C.RESET} Invalid option")

        input(f"\n{C.DIM}Press Enter...{C.RESET}")
