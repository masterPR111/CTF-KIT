"""
Flag Tracker Module - SQLite database
"""
import sqlite3
import os
import csv
from datetime import datetime
from config import Colors as C, DATA_DIR, DB_PATH


def init_db():
    os.makedirs(DATA_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS flags (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ctf_name TEXT NOT NULL,
        challenge TEXT NOT NULL,
        category TEXT,
        flag TEXT NOT NULL,
        points INTEGER DEFAULT 0,
        notes TEXT,
        timestamp TEXT
    )''')
    conn.commit()
    return conn


def run():
    while True:
        print(f"""{C.CYAN}{C.BOLD}
    ╔═══════════════════════════════════════════╗
    ║            FLAG TRACKER                   ║
    ╠═══════════════════════════════════════════╣
    ║  {C.WHITE}[1]{C.CYAN}  Add Flag                             ║
    ║  {C.WHITE}[2]{C.CYAN}  List All Flags                      ║
    ║  {C.WHITE}[3]{C.CYAN}  Statistics                          ║
    ║  {C.WHITE}[4]{C.CYAN}  Search Flag                         ║
    ║  {C.WHITE}[5]{C.CYAN}  Export to CSV                       ║
    ║  {C.WHITE}[6]{C.CYAN}  Delete Flag                         ║
    ║  {C.WHITE}[0]{C.CYAN}  Back                                ║
    ╚═══════════════════════════════════════════╝
        {C.RESET}""")

        choice = input(f"{C.MAGENTA}[?]{C.RESET} Select option: ").strip()

        if choice == "0":
            return
        elif choice == "1":
            ctf = input(f"{C.MAGENTA}[?]{C.RESET} CTF name: ")
            challenge = input(f"{C.MAGENTA}[?]{C.RESET} Challenge: ")
            category = input(f"{C.MAGENTA}[?]{C.RESET} Category: ")
            flag = input(f"{C.MAGENTA}[?]{C.RESET} Flag: ")
            points = int(input(f"{C.MAGENTA}[?]{C.RESET} Points [0]: ") or "0")
            notes = input(f"{C.MAGENTA}[?]{C.RESET} Notes: ")
            conn = init_db()
            c = conn.cursor()
            c.execute('''INSERT INTO flags (ctf_name, challenge, category, flag, points, notes, timestamp)
                         VALUES (?, ?, ?, ?, ?, ?, ?)''',
                      (ctf, challenge, category, flag, points, notes, datetime.now().isoformat()))
            conn.commit()
            conn.close()
            print(f"{C.GREEN}[+]{C.RESET} Flag added!")
        elif choice == "2":
            conn = init_db()
            c = conn.cursor()
            c.execute('SELECT * FROM flags ORDER BY timestamp DESC')
            rows = c.fetchall()
            conn.close()
            if rows:
                for row in rows:
                    print(f"  {C.YELLOW}[{row[0]}]{C.RESET} {row[1]} / {row[2]} / {row[3]}")
                    print(f"      {C.GREEN}{row[4]}{C.RESET} ({row[5]} pts)")
            else:
                print(f"{C.YELLOW}[!]{C.RESET} No flags yet")
        elif choice == "3":
            conn = init_db()
            c = conn.cursor()
            c.execute('SELECT COUNT(*), SUM(points) FROM flags')
            count, total = c.fetchone()
            conn.close()
            print(f"  Total flags: {C.GREEN}{count}{C.RESET}")
            print(f"  Total points: {C.GREEN}{total or 0}{C.RESET}")
        elif choice == "4":
            query = input(f"{C.MAGENTA}[?]{C.RESET} Search: ")
            conn = init_db()
            c = conn.cursor()
            c.execute('SELECT * FROM flags WHERE flag LIKE ? OR challenge LIKE ?',
                      (f'%{query}%', f'%{query}%'))
            rows = c.fetchall()
            conn.close()
            for row in rows:
                print(f"  {C.GREEN}{row[4]}{C.RESET} ({row[2]})")
        elif choice == "5":
            conn = init_db()
            c = conn.cursor()
            c.execute('SELECT * FROM flags ORDER BY timestamp DESC')
            rows = c.fetchall()
            conn.close()
            filename = f"flags_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['ID', 'CTF', 'Challenge', 'Category', 'Flag', 'Points', 'Notes', 'Timestamp'])
                writer.writerows(rows)
            print(f"{C.GREEN}[+]{C.RESET} Exported to {filename}")
        elif choice == "6":
            flag_id = input(f"{C.MAGENTA}[?]{C.RESET} Flag ID: ")
            conn = init_db()
            c = conn.cursor()
            c.execute('DELETE FROM flags WHERE id = ?', (flag_id,))
            conn.commit()
            conn.close()
            print(f"{C.GREEN}[+]{C.RESET} Deleted")
        else:
            print(f"{C.RED}[-]{C.RESET} Invalid option")

        input(f"\n{C.DIM}Press Enter...{C.RESET}")
