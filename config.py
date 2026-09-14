"""
CTFKit Configuration
"""
import os

VERSION = "1.0.0"
AUTHOR = "Your Name"
GITHUB = "https://github.com/YOUR_USERNAME/ctfkit"


class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RESET = '\033[0m'


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WORDLIST_DIR = os.path.join(BASE_DIR, "wordlists")
DATA_DIR = os.path.join(BASE_DIR, "data")
DB_PATH = os.path.join(DATA_DIR, "flags.db")

DEFAULT_WORDLIST = "/usr/share/wordlists/dirb/common.txt"
SUBDOMAIN_WORDLIST = "/usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt"

HTTP_TIMEOUT = 10
COMMAND_TIMEOUT = 300

FLAG_PATTERNS = [
    r'[A-Za-z0-9_]+\{[^}]+\}',
    r'flag\{[^}]+\}',
    r'FLAG\{[^}]+\}',
    r'CTF\{[^}]+\}',
    r'HTB\{[^}]+\}',
    r'THM\{[^}]+\}',
]
