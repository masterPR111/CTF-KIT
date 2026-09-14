"""
Forensics Module
"""
import subprocess
from config import Colors as C


def run_cmd(cmd):
    print(f"{C.BLUE}[*]{C.RESET} {cmd}")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True,
                                text=True, timeout=300)
        if result.stdout:
            print(result.stdout[:3000])
        if result.stderr:
            print(f"{C.YELLOW}[!]{C.RESET} {result.stderr[:300]}")
    except Exception as e:
        print(f"{C.RED}[-]{C.RESET} {e}")


def run():
    while True:
        print(f"""{C.CYAN}{C.BOLD}
    ╔═══════════════════════════════════════════╗
    ║             FORENSICS                     ║
    ╠═══════════════════════════════════════════╣
    ║  {C.WHITE}[1]{C.CYAN}  File Type Detection                  ║
    ║  {C.WHITE}[2]{C.CYAN}  Strings Extraction                   ║
    ║  {C.WHITE}[3]{C.CYAN}  Metadata (exiftool)                 ║
    ║  {C.WHITE}[4]{C.CYAN}  Steganography (steghide)            ║
    ║  {C.WHITE}[5]{C.CYAN}  Binwalk Analysis                    ║
    ║  {C.WHITE}[6]{C.CYAN}  Hexdump                             ║
    ║  {C.WHITE}[7]{C.CYAN}  File Carving (foremost)             ║
    ║  {C.WHITE}[0]{C.CYAN}  Back                                ║
    ╚═══════════════════════════════════════════╝
        {C.RESET}""")

        choice = input(f"{C.MAGENTA}[?]{C.RESET} Select option: ").strip()

        if choice == "0":
            return
        elif choice == "1":
            f = input(f"{C.MAGENTA}[?]{C.RESET} File: ")
            run_cmd(f"file {f}")
        elif choice == "2":
            f = input(f"{C.MAGENTA}[?]{C.RESET} File: ")
            run_cmd(f"strings {f} | head -100")
        elif choice == "3":
            f = input(f"{C.MAGENTA}[?]{C.RESET} File: ")
            run_cmd(f"exiftool {f}")
        elif choice == "4":
            f = input(f"{C.MAGENTA}[?]{C.RESET} File: ")
            passphrase = input(f"{C.MAGENTA}[?]{C.RESET} Passphrase (blank): ")
            if passphrase:
                run_cmd(f"steghide extract -sf {f} -p '{passphrase}'")
            else:
                run_cmd(f"steghide info {f}")
        elif choice == "5":
            f = input(f"{C.MAGENTA}[?]{C.RESET} File: ")
            run_cmd(f"binwalk {f}")
        elif choice == "6":
            f = input(f"{C.MAGENTA}[?]{C.RESET} File: ")
            run_cmd(f"xxd {f} | head -50")
        elif choice == "7":
            f = input(f"{C.MAGENTA}[?]{C.RESET} File: ")
            run_cmd(f"foremost -i {f} -o output/")
        else:
            print(f"{C.RED}[-]{C.RESET} Invalid option")

        input(f"\n{C.DIM}Press Enter...{C.RESET}")
