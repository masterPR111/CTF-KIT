# 🚀 CTF-KIT — All-in-One CTF Toolkit

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey)
![Made in Sri Lanka](https://img.shields.io/badge/Made%20in-Sri%20Lanka%20🇱🇰-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

A professional, all-in-one toolkit for **Capture The Flag (CTF)** competitions, **bug bounty hunting**, and **penetration testing**. Built with ❤️ in Sri Lanka.

---

## ✨ Features

| Module | Features |
|--------|----------|
| 🔐 **Encoding/Decoding** | Base64, Hex, URL, ROT13, Binary, ASCII, Morse |
| 🔢 **Hashing** | MD5, SHA1, SHA256, SHA512, File hashing |
| 🔄 **Cipher Tools** | Caesar, XOR, Vigenère, Atbash, Flag regex |
| 🌐 **Web Recon** | ffuf, nmap, whatweb, subdomain enum, common files |
| 💥 **Web Exploitation** | SQLi, XSS, LFI, CMDi, SSRF, JWT, CORS, GraphQL |
| 🛠️ **Misc Tools** | Reverse shells, payloads, JWT, DNS, Whois |
| 🔒 **Crypto Attacks** | RSA, Frequency analysis, Prime factorization |
| 🔍 **Forensics** | Steghide, binwalk, exiftool, strings |
| 🚩 **Flag Tracker** | SQLite database for CTF flags |
| 🎨 **Beautiful CLI** | Colorful menus, animations, progress bars |

---

## 📸 Screenshots

```
╔═══════════════════════════════════════════════════════════╗
║   ██████╗████████╗███████╗    ██╗  ██╗██╗████████╗        ║
║  ██╔════╝╚══██╔══╝██╔════╝    ██║ ██╔╝██║╚══██╔══╝        ║
║  ██║        ██║   █████╗      █████╔╝ ██║   ██║           ║
║  ██║        ██║   ██╔══╝      ██╔═██╗ ██║   ██║           ║
║  ╚██████╗   ██║   ██║         ██║  ██╗██║   ██║           ║
║   ╚═════╝   ╚═╝   ╚═╝         ╚═╝  ╚═╝╚═╝   ╚═╝           ║
║           All-in-One CTF Toolkit v1.0                     ║
║           Made in Sri Lanka 🇱🇰                            ║
╚═══════════════════════════════════════════════════════════╝
```

---

## 📦 Installation

### ⚡ One-Line Install (Fastest!)

**Copy-paste කරන්න:**

```bash
git clone https://github.com/masterPR111/CTF-KIT.git && cd CTF-KIT && chmod +x auto_install.sh && ./auto_install.sh
```

**එච්චරයි!** එක command එකකින් **ඔක්කොම install** වෙනවා. ✅

---

### 🚀 Auto-Install (Recommended)

**Step 1: Clone the repository**

```bash
git clone https://github.com/masterPR111/CTF-KIT.git
cd CTF-KIT
```

**Step 2: Run auto-installer**

```bash
chmod +x auto_install.sh
./auto_install.sh
```

**හෝ sudo සමඟ (system tools සඳහා):**

```bash
sudo ./auto_install.sh
```

**Step 3: Run CTF-KIT**

```bash
python3 ctfkit.py
```

---

### 📋 What Auto-Install Does

මේ **script** එක **automatically**:

- ✅ **Python dependencies** install කරනවා (`requirements.txt`)
- ✅ **System tools** install කරනවා (`requirements2.txt`)
- ✅ **OS detect** කරනවා (Ubuntu, Kali, Arch, Fedora, macOS)
- ✅ **Already installed** tools **skip** කරනවා
- ✅ **Summary** එකක් පෙන්නනවා (Success/Failed count)
- ✅ **Permissions** set කරනවා

---

### 📋 Tools That Get Installed

| Category | Tools |
|----------|-------|
| **Recon** | nmap, ffuf, gobuster, dirb, whatweb, whois, dnsutils |
| **Web** | sqlmap, nikto, wpscan |
| **Password** | hashcat, john, hydra |
| **Forensics** | steghide, binwalk, exiftool, foremost |
| **Network** | tcpdump, wireshark, netcat |
| **Reverse Engineering** | gdb, radare2 |
| **Wordlists** | seclists, wordlists |
| **Python** | requests, bs4, pycryptodome, rich, etc. |

---

### 🎯 Supported Operating Systems

| OS | Package Manager | Auto-Detect | Status |
|----|----------------|-------------|--------|
| Ubuntu | apt | ✅ | Full support |
| Debian | apt | ✅ | Full support |
| Kali Linux | apt | ✅ | Full support |
| Parrot OS | apt | ✅ | Full support |
| Arch Linux | pacman | ✅ | Full support |
| Manjaro | pacman | ✅ | Full support |
| Fedora | dnf | ✅ | Full support |
| RHEL / CentOS | dnf | ✅ | Full support |
| macOS | brew | ✅ | Full support |

---

### 🐳 Docker Install

**Build image:**

```bash
docker build -t ctf-kit .
```

**Run container:**

```bash
docker run -it --rm --network host ctf-kit
```

---

### ⚠️ Requirements

**Minimum:**

- Python 3.8+
- pip3
- Internet connection
- git

**Optional (recommended):**

- Kali Linux (all tools pre-installed)
- sudo access (for system tools)

---

### 🔧 If Auto-Install Fails

**Permission issues:**

```bash
sudo ./auto_install.sh
```

**Python module issues:**

```bash
pip3 install --user -r requirements.txt
```

**System tool issues:**

```bash
# Ubuntu/Debian/Kali
sudo apt install -y ffuf nmap whatweb whois dnsutils

# Arch
sudo pacman -S --noconfirm ffuf nmap whatweb whois bind

# Fedora
sudo dnf install -y ffuf nmap whatweb whois bind-utils
```

**PATH warning (`~/.local/bin not on PATH`):**

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

---

## 🎯 Usage

### Interactive Menu

```bash
python3 ctfkit.py
```

**Main Menu:**

```
╔═══════════════════════════════════════════╗
║              MAIN MENU                    ║
╠═══════════════════════════════════════════╣
║  [1]  🔐 Encoding / Decoding              ║
║  [2]  🔢 Hashing                          ║
║  [3]  🔄 Cipher Tools                     ║
║  [4]  🌐 Web Recon                        ║
║  [5]  💥 Web Exploitation                 ║
║  [6]  🛠️  Misc Tools                       ║
║  [7]  🔒 Crypto Attacks                   ║
║  [8]  🔍 Forensics                        ║
║  [9]  🚩 Flag Tracker                     ║
║  [0]  🚪 Exit                             ║
╚═══════════════════════════════════════════╝
```

---

## 📋 Requirements

### Python
- Python 3.8+
- See `requirements.txt`

### System Tools
- See `requirements2.txt`
- Auto-installed by `auto_install.sh`

> **Note:** System tools නැතුවත් CTF-KIT වැඩ කරනවා — Python fallbacks තියෙනවා.

---

## 🐛 Troubleshooting

### Error: `ModuleNotFoundError`

```bash
pip3 install -r requirements.txt
```

### Error: `Permission denied`

```bash
chmod +x ctfkit.py auto_install.sh
```

### Error: `ffuf: command not found`

```bash
sudo apt install ffuf
```

### Warning: `~/.local/bin not on PATH`

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## ⚠️ Disclaimer

This tool is for **educational purposes** and **authorized testing only**. Do not use it against systems you don't have permission to test. The author is not responsible for any misuse.

---

## 🙏 Acknowledgments

- Thanks to the CTF community in Sri Lanka 🇱🇰
- Special thanks to all contributors

---

## 📞 Contact

- **Author**: Master PR
- **GitHub**: [@masterPR111](https://github.com/masterPR111)

---

<div align="center">

**⭐ Star this repo if you find it useful! ⭐**

**Made with ❤️ in Sri Lanka 🇱🇰**

</div>
