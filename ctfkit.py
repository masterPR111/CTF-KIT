#!/usr/bin/env python3
"""
CTFKit - All-in-One CTF Toolkit
Beautiful UI without external dependencies
"""
import os
import sys
import signal
import shutil

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ui import (
    C, clear, show_banner, show_banner_animated, show_menu,
    ask, confirm, pause, print_success, print_error, print_warning,
    print_info, print_section, print_finding, print_table,
    progress_bar, spinner, typewriter, fade_in, matrix_rain,
    show_tool_status, hide_cursor, show_cursor
)
from modules import (
    encoding, hashing, cipher, web_recon, web_exploit,
    misc, crypto, forensics, flag_tracker
)


# ============================================================
# SYSTEM TOOLS CHECK
# ============================================================
REQUIRED_TOOLS = {
    "ffuf": "sudo apt install ffuf",
    "nmap": "sudo apt install nmap",
    "whatweb": "sudo apt install whatweb",
    "whois": "sudo apt install whois",
    "dig": "sudo apt install dnsutils",
    "steghide": "sudo apt install steghide",
    "binwalk": "sudo apt install binwalk",
    "exiftool": "sudo apt install exiftool",
    "hashcat": "sudo apt install hashcat",
    "john": "sudo apt install john",
}


def check_system_tools():
    """Check which tools are available"""
    available = []
    missing = []
    
    for tool, cmd in REQUIRED_TOOLS.items():
        if shutil.which(tool):
            available.append(tool)
        else:
            missing.append((tool, cmd))
    
    return available, missing


# ============================================================
# MENU
# ============================================================
MENU_OPTIONS = [
    ("1", "🔐", "Encoding / Decoding"),
    ("2", "🔢", "Hashing"),
    ("3", "🔄", "Cipher Tools"),
    ("4", "🌐", "Web Reconnaissance"),
    ("5", "💥", "Web Exploitation"),
    ("6", "🛠️ ", "Misc Tools"),
    ("7", "🔒", "Crypto Attacks"),
    ("8", "🔍", "Forensics"),
    ("9", "🚩", "Flag Tracker"),
    ("0", "🚪", "Exit"),
]


def main_menu():
    """Main menu loop"""
    while True:
        show_menu(MENU_OPTIONS, "MAIN MENU")
        
        choice = ask("Select option")
        
        if choice == "0":
            print()
            print(f"  {C.BGREEN}{C.BOLD} Goodbye! Happy Hacking! 🚀 {C.RESET}")
            print()
            sys.exit(0)
        elif choice == "1":
            encoding.run()
        elif choice == "2":
            hashing.run()
        elif choice == "3":
            cipher.run()
        elif choice == "4":
            web_recon.run()
        elif choice == "5":
            web_exploit.run()
        elif choice == "6":
            misc.run()
        elif choice == "7":
            crypto.run()
        elif choice == "8":
            forensics.run()
        elif choice == "9":
            flag_tracker.run()
        else:
            print_error("Invalid option")
            pause()


# ============================================================
# SPLASH
# ============================================================
def splash_screen():
    """Show splash screen"""
    show_banner_animated()
    
    print(f"  {C.BCYAN}{C.BOLD}Initializing CTFKit...{C.RESET}")
    print()
    
    # Spinner animation
    spinner("Loading modules", 1)
    spinner("Checking system tools", 1)
    spinner("Preparing interface", 0.5)
    
    # Check tools
    available, missing = check_system_tools()
    show_tool_status(available, missing)
    
    if missing:
        print_warning(f"{len(missing)} system tools missing - some features disabled")
        print_info("Install with: sudo apt install <tool>")
    
    pause()


# ============================================================
# SIGNAL HANDLER
# ============================================================
def signal_handler(sig, frame):
    show_cursor()
    print()
    print(f"  {C.BYELLOW}{C.BOLD}[!]{C.RESET} {C.YELLOW}Interrupted. Goodbye!{C.RESET}")
    sys.exit(0)


# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    try:
        splash_screen()
        main_menu()
    except KeyboardInterrupt:
        show_cursor()
        print()
        print(f"  {C.BYELLOW}[!]{C.RESET} Goodbye!")
        sys.exit(0)
    finally:
        show_cursor()
