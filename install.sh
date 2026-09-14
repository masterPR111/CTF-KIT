#!/bin/bash
# CTFKit Installation Script

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

echo -e "${CYAN}"
cat << "EOF"
   _____ _______ ______ _  _______ _____ 
  / ____|__   __|  ____| |/ /_   _|_   _|
 | |       | |  | |__  | ' /  | |   | |  
 | |       | |  |  __| |  <   | |   | |  
 | |____   | |  | |    | . \ _| |_ _| |_ 
  \_____|  |_|  |_|    |_|\_\_____|_____|
                                         
     All-in-One CTF Toolkit Installer
EOF
echo -e "${NC}"

if ! command -v python3 &> /dev/null; then
    echo -e "${RED}[!] Python3 not found. Please install Python 3.8+${NC}"
    exit 1
fi

echo -e "${GREEN}[+] Python3: $(python3 --version)${NC}"

echo -e "${CYAN}[*] Installing Python dependencies...${NC}"
pip3 install -r requirements.txt

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    if command -v apt &> /dev/null; then
        echo -e "${CYAN}[*] Installing system tools (Debian/Ubuntu)...${NC}"
        sudo apt update
        sudo apt install -y ffuf nmap whatweb whois dnsutils \
            steghide binwalk exiftool hashcat john gobuster
    elif command -v pacman &> /dev/null; then
        echo -e "${CYAN}[*] Installing system tools (Arch)...${NC}"
        sudo pacman -S --noconfirm ffuf nmap whatweb whois bind \
            steghide binwalk exiftool hashcat john gobuster
    fi
elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo -e "${CYAN}[*] Installing via Homebrew...${NC}"
    brew install ffuf nmap whatweb whois bind steghide binwalk exiftool hashcat john gobuster
fi

chmod +x ctfkit.py

echo -e "${GREEN}"
echo "============================================"
echo "  ✅ CTFKit installed successfully!"
echo "============================================"
echo -e "${NC}"
echo -e "Run: ${CYAN}python3 ctfkit.py${NC}"
