#!/bin/bash
# ============================================
# CTFKit Auto-Install Script
# Reads requirements2.txt and installs everything
# ============================================

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

# Banner
echo -e "${CYAN}${BOLD}"
cat << "EOF"
    ╔═══════════════════════════════════════════════╗
    ║                                               ║
    ║   ██████╗████████╗███████╗    ██╗  ██╗██╗████████╗
    ║  ██╔════╝╚══██╔══╝██╔════╝    ██║ ██╔╝██║╚══██╔══╝
    ║  ██║        ██║   █████╗      █████╔╝ ██║   ██║
    ║  ██║        ██║   ██╔══╝      ██╔═██╗ ██║   ██║
    ║  ╚██████╗   ██║   ██║         ██║  ██╗██║   ██║
    ║   ╚═════╝   ╚═╝   ╚═╝         ╚═╝  ╚═╝╚═╝   ╚═╝
    ║                                               ║
    ║           Auto-Install Script v1.0            ║
    ║           Made in Sri Lanka 🇱🇰                  ║
    ╚═══════════════════════════════════════════════╝
EOF
echo -e "${NC}"

# ============ CHECK ROOT ============
if [ "$EUID" -ne 0 ]; then
    echo -e "${YELLOW}[!]${NC} Running without sudo. Some installs may fail."
    echo -e "${YELLOW}[!]${NC} Tip: Run with 'sudo ./auto_install.sh' for best results."
    echo ""
fi

# ============ DETECT OS ============
detect_os() {
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        OS=$ID
    elif [ -f /etc/debian_version ]; then
        OS="debian"
    elif [ -f /etc/arch-release ]; then
        OS="arch"
    elif [ -f /etc/fedora-release ]; then
        OS="fedora"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macos"
    else
        OS="unknown"
    fi
    echo -e "${CYAN}[*]${NC} Detected OS: ${BOLD}$OS${NC}"
}

# ============ CHECK COMMAND ============
command_exists() {
    command -v "$1" &> /dev/null
}

# ============ INSTALL WITH CHECK ============
install_tool() {
    local cmd="$1"
    local desc="$2"
    
    # Extract tool name from command
    local tool_name=$(echo "$cmd" | awk '{print $NF}')
    
    # Skip if already installed (for apt tools)
    if [[ "$cmd" == sudo\ apt\ install* ]]; then
        if dpkg -l 2>/dev/null | grep -q "^ii  $tool_name "; then
            echo -e "  ${GREEN}✅${NC} $tool_name ${CYAN}(already installed)${NC} - $desc"
            return 0
        fi
    fi
    
    # Skip if command exists
    if command_exists "$tool_name"; then
        echo -e "  ${GREEN}✅${NC} $tool_name ${CYAN}(already installed)${NC} - $desc"
        return 0
    fi
    
    # Install
    echo -e "  ${YELLOW}⏳${NC} Installing $tool_name... - $desc"
    
    if eval "$cmd" &> /dev/null; then
        echo -e "  ${GREEN}✅${NC} $tool_name installed successfully"
        return 0
    else
        echo -e "  ${RED}❌${NC} $tool_name installation failed"
        return 1
    fi
}

# ============ MAIN INSTALL ============
main_install() {
    local req_file="$1"
    
    if [ ! -f "$req_file" ]; then
        echo -e "${RED}[-]${NC} File not found: $req_file"
        exit 1
    fi
    
    echo -e "\n${CYAN}${BOLD}[*] Reading: $req_file${NC}\n"
    
    local total=0
    local success=0
    local failed=0
    local skipped=0
    
    # Read each line
    while IFS='|' read -r cmd desc; do
        # Skip empty lines and comments
        [[ -z "$cmd" || "$cmd" =~ ^# ]] && continue
        
        # Trim whitespace
        cmd=$(echo "$cmd" | xargs)
        desc=$(echo "$desc" | xargs)
        
        total=$((total + 1))
        
        if install_tool "$cmd" "$desc"; then
            success=$((success + 1))
        else
            failed=$((failed + 1))
        fi
    done < "$req_file"
    
    # Summary
    echo ""
    echo -e "${CYAN}${BOLD}═══════════════════════════════════════════════${NC}"
    echo -e "${CYAN}${BOLD}  INSTALLATION SUMMARY${NC}"
    echo -e "${CYAN}${BOLD}═══════════════════════════════════════════════${NC}"
    echo -e "  Total:     ${BOLD}$total${NC}"
    echo -e "  ${GREEN}Success:   $success${NC}"
    echo -e "  ${RED}Failed:    $failed${NC}"
    echo -e "${CYAN}${BOLD}═══════════════════════════════════════════════${NC}"
    
    if [ $failed -eq 0 ]; then
        echo -e "\n${GREEN}${BOLD}✅ All tools installed successfully!${NC}\n"
    else
        echo -e "\n${YELLOW}${BOLD}⚠️  Some tools failed to install.${NC}"
        echo -e "${YELLOW}Try running with sudo:${NC}"
        echo -e "  ${CYAN}sudo ./auto_install.sh${NC}\n"
    fi
}

# ============ MAIN ============
main() {
    detect_os
    
    # Check Python
    if ! command_exists python3; then
        echo -e "${RED}[-]${NC} Python3 not found!"
        echo -e "${YELLOW}[!]${NC} Install Python 3.8+ first."
        exit 1
    fi
    echo -e "${GREEN}[+]${NC} Python3: $(python3 --version)"
    
    # Update package list (Debian/Ubuntu)
    if [[ "$OS" == "ubuntu" || "$OS" == "debian" || "$OS" == "kali" ]]; then
        echo -e "\n${CYAN}[*]${NC} Updating package list..."
        sudo apt update -qq 2>/dev/null || true
    fi
    
    # Install from requirements2.txt
    main_install "requirements2.txt"
    
    # Final message
    echo -e "${CYAN}${BOLD}Next steps:${NC}"
    echo -e "  1. Run: ${CYAN}python3 ctfkit.py${NC}"
    echo -e "  2. Enjoy hacking! 🚀\n"
}

# Run
main "$@"
