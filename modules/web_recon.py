"""
Web Reconnaissance Module
"""
import subprocess
from config import Colors as C, DEFAULT_WORDLIST, SUBDOMAIN_WORDLIST, COMMAND_TIMEOUT


def run_cmd(cmd, timeout=COMMAND_TIMEOUT):
    print(f"{C.BLUE}[*]{C.RESET} Running: {cmd}")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True,
                                text=True, timeout=timeout)
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(f"{C.YELLOW}[!]{C.RESET} {result.stderr[:500]}")
        return result.stdout
    except subprocess.TimeoutExpired:
        print(f"{C.RED}[-]{C.RESET} Command timed out")
        return ""
    except FileNotFoundError:
        print(f"{C.RED}[-]{C.RESET} Command not found: {cmd.split()[0]}")
        return ""


def full_recon(target):
    print(f"\n{C.BOLD}=== FULL RECON: {target} ==={C.RESET}\n")
    
    print(f"{C.CYAN}[*]{C.RESET} 1. HTTP Headers")
    run_cmd(f"curl -I {target}")
    
    print(f"\n{C.CYAN}[*]{C.RESET} 2. Robots.txt")
    run_cmd(f"curl -s {target}/robots.txt")
    
    print(f"\n{C.CYAN}[*]{C.RESET} 3. Technology Detection")
    run_cmd(f"whatweb {target}")
    
    print(f"\n{C.CYAN}[*]{C.RESET} 4. Common Files")
    common_files = ['.git/config', '.env', 'backup.zip', 'db.sql', 'config.php']
    for f in common_files:
        try:
            code = subprocess.run(
                f"curl -s -o /dev/null -w '%{{http_code}}' {target}/{f}",
                shell=True, capture_output=True, text=True, timeout=10
            ).stdout
            if code not in ["404", "000"]:
                print(f"  {C.GREEN}✅ {code}  /{f}{C.RESET}")
        except:
            pass
    
    print(f"\n{C.CYAN}[*]{C.RESET} 5. Directory Brute-force")
    run_cmd(f"ffuf -u {target}/FUZZ -w {DEFAULT_WORDLIST} -mc 200,301,302,401,403 -t 50 -s", timeout=600)


def run():
    while True:
        print(f"""{C.CYAN}{C.BOLD}
    ╔═══════════════════════════════════════════╗
    ║            WEB RECON                      ║
    ╠═══════════════════════════════════════════╣
    ║  {C.WHITE}[1]{C.CYAN}  Full Recon                          ║
    ║  {C.WHITE}[2]{C.CYAN}  Directory Brute-force (ffuf)        ║
    ║  {C.WHITE}[3]{C.CYAN}  Subdomain Enumeration               ║
    ║  {C.WHITE}[4]{C.CYAN}  Port Scan (nmap)                    ║
    ║  {C.WHITE}[5]{C.CYAN}  Technology Detection (whatweb)      ║
    ║  {C.WHITE}[6]{C.CYAN}  Robots.txt / Sitemap                ║
    ║  {C.WHITE}[7]{C.CYAN}  Common Files Check                  ║
    ║  {C.WHITE}[8]{C.CYAN}  HTTP Headers                        ║
    ║  {C.WHITE}[0]{C.CYAN}  Back                                ║
    ╚═══════════════════════════════════════════╝
        {C.RESET}""")

        choice = input(f"{C.MAGENTA}[?]{C.RESET} Select option: ").strip()

        if choice == "0":
            return
        elif choice == "1":
            target = input(f"{C.MAGENTA}[?]{C.RESET} Target URL: ")
            full_recon(target)
        elif choice == "2":
            target = input(f"{C.MAGENTA}[?]{C.RESET} Target URL: ")
            wl = input(f"{C.MAGENTA}[?]{C.RESET} Wordlist [{DEFAULT_WORDLIST}]: ") or DEFAULT_WORDLIST
            run_cmd(f"ffuf -u {target}/FUZZ -w {wl} -mc 200,301,302,401,403 -t 50")
        elif choice == "3":
            domain = input(f"{C.MAGENTA}[?]{C.RESET} Domain: ")
            wl = input(f"{C.MAGENTA}[?]{C.RESET} Wordlist [{SUBDOMAIN_WORDLIST}]: ") or SUBDOMAIN_WORDLIST
            run_cmd(f"ffuf -u http://{domain}/ -H 'Host: FUZZ.{domain}' -w {wl} -mc 200,301,302,401,403 -fs 0")
        elif choice == "4":
            target = input(f"{C.MAGENTA}[?]{C.RESET} Target: ")
            ports = input(f"{C.MAGENTA}[?]{C.RESET} Ports [1-10000]: ") or "1-10000"
            run_cmd(f"nmap -p {ports} --min-rate 5000 -sV {target}")
        elif choice == "5":
            target = input(f"{C.MAGENTA}[?]{C.RESET} Target URL: ")
            run_cmd(f"whatweb {target}")
        elif choice == "6":
            target = input(f"{C.MAGENTA}[?]{C.RESET} Target URL: ")
            run_cmd(f"curl -s {target}/robots.txt")
            run_cmd(f"curl -s {target}/sitemap.xml")
        elif choice == "7":
            target = input(f"{C.MAGENTA}[?]{C.RESET} Target URL: ")
            common_files = ['.git/config', '.env', 'backup.zip', 'db.sql',
                            'config.php', 'wp-config.php', '.htaccess',
                            'phpinfo.php', '.DS_Store']
            for f in common_files:
                try:
                    code = subprocess.run(
                        f"curl -s -o /dev/null -w '%{{http_code}}' {target}/{f}",
                        shell=True, capture_output=True, text=True, timeout=10
                    ).stdout
                    if code not in ["404", "000"]:
                        print(f"  {C.GREEN}✅ {code}  /{f}{C.RESET}")
                except:
                    pass
        elif choice == "8":
            target = input(f"{C.MAGENTA}[?]{C.RESET} Target URL: ")
            run_cmd(f"curl -I {target}")
        else:
            print(f"{C.RED}[-]{C.RESET} Invalid option")

        input(f"\n{C.DIM}Press Enter...{C.RESET}")
