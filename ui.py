"""
CTFKit UI - Beautiful terminal interface (no external dependencies)
Pure Python + ANSI escape codes
"""
import os
import sys
import time
import shutil
import textwrap


# ============================================================
# COLORS (ANSI)
# ============================================================
class C:
    # Basic colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright colors
    BRED = '\033[91m'
    BGREEN = '\033[92m'
    BYELLOW = '\033[93m'
    BBLUE = '\033[94m'
    BMAGENTA = '\033[95m'
    BCYAN = '\033[96m'
    BWHITE = '\033[97m'
    
    # Styles
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    
    # Background
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    
    RESET = '\033[0m'


# ============================================================
# TERMINAL UTILS
# ============================================================
def get_terminal_width():
    """Get terminal width"""
    try:
        return shutil.get_terminal_size().columns
    except:
        return 80


def clear():
    """Clear screen"""
    os.system('clear' if os.name != 'nt' else 'cls')


def hide_cursor():
    """Hide cursor"""
    sys.stdout.write('\033[?25l')
    sys.stdout.flush()


def show_cursor():
    """Show cursor"""
    sys.stdout.write('\033[?25h')
    sys.stdout.flush()


def move_cursor(x, y):
    """Move cursor to position"""
    sys.stdout.write(f'\033[{y};{x}H')
    sys.stdout.flush()


# ============================================================
# BANNER
# ============================================================
BANNER_LINES = [
    "    ╔═══════════════════════════════════════════════════════════╗",
    "    ║                                                           ║",
    "    ║   ██████╗████████╗███████╗    ██╗  ██╗██╗████████╗        ║",
    "    ║  ██╔════╝╚══██╔══╝██╔════╝    ██║ ██╔╝██║╚══██╔══╝        ║",
    "    ║  ██║        ██║   █████╗      █████╔╝ ██║   ██║           ║",
    "    ║  ██║        ██║   ██╔══╝      ██╔═██╗ ██║   ██║           ║",
    "    ║  ╚██████╗   ██║   ██║         ██║  ██╗██║   ██║           ║",
    "    ║   ╚═════╝   ╚═╝   ╚═╝         ╚═╝  ╚═╝╚═╝   ╚═╝           ║",
    "    ║                                                           ║",
    "    ║           All-in-One CTF Toolkit v1.0                     ║",
    "    ║           Made in Sri Lanka 🇱🇰                            ║",
    "    ╚═══════════════════════════════════════════════════════════╝",
]


def show_banner():
    """Display banner with gradient colors"""
    clear()
    print()
    for i, line in enumerate(BANNER_LINES):
        # Gradient effect
        if i < 4:
            color = C.BCYAN
        elif i < 8:
            color = C.CYAN
        elif i < 10:
            color = C.BBLUE
        else:
            color = C.BLUE
        
        print(f"{color}{C.BOLD}{line}{C.RESET}")
    print()


def show_banner_animated():
    """Animated banner (typewriter effect)"""
    clear()
    print()
    for line in BANNER_LINES:
        print(f"{C.BCYAN}{C.BOLD}{line}{C.RESET}")
        time.sleep(0.05)
    print()


# ============================================================
# BOX DRAWING
# ============================================================
def draw_box(lines, title="", width=None, color=C.CYAN, padding=1):
    """Draw a box around lines"""
    if width is None:
        width = max(len(line) for line in lines) + (padding * 2) + 2
    
    if title:
        title_str = f" {title} "
        title_len = len(title_str)
        left = (width - title_len) // 2
        right = width - title_len - left
        top = f"╭{'─' * left}{title_str}{'─' * right}╮"
    else:
        top = f"╭{'─' * width}╮"
    
    bottom = f"╰{'─' * width}╯"
    
    print(f"{color}{top}{C.RESET}")
    for line in lines:
        padded = line.ljust(width - padding * 2)
        print(f"{color}│{C.RESET}{' ' * padding}{padded}{' ' * padding}{color}│{C.RESET}")
    print(f"{color}{bottom}{C.RESET}")


def draw_double_box(lines, title="", width=None, color=C.BCYAN):
    """Draw a double-line box"""
    if width is None:
        width = max(len(line) for line in lines) + 4
    
    if title:
        title_str = f" {title} "
        title_len = len(title_str)
        left = (width - title_len) // 2
        right = width - title_len - left
        top = f"╔{'═' * left}{title_str}{'═' * right}╗"
    else:
        top = f"╔{'═' * width}╗"
    
    bottom = f"╚{'═' * width}╝"
    
    print(f"{color}{C.BOLD}{top}{C.RESET}")
    for line in lines:
        padded = line.ljust(width - 2)
        print(f"{color}{C.BOLD}║{C.RESET} {padded} {color}{C.BOLD}║{C.RESET}")
    print(f"{color}{C.BOLD}{bottom}{C.RESET}")


# ============================================================
# MENU
# ============================================================
def show_menu(options, title="MENU"):
    """Display a beautiful menu"""
    show_banner()
    
    # Calculate width
    max_label = max(len(label) for _, _, label in options)
    width = max_label + 15
    
    print(f"{C.BCYAN}{C.BOLD}    ╭{'─' * (width + 4)}╮{C.RESET}")
    
    # Title
    title_str = f" {title} "
    padding = (width + 4 - len(title_str)) // 2
    print(f"{C.BCYAN}{C.BOLD}    │{' ' * padding}{C.BYELLOW}{title_str}{C.BCYAN}{' ' * (width + 4 - padding - len(title_str))}│{C.RESET}")
    print(f"{C.BCYAN}{C.BOLD}    ├{'─' * (width + 4)}┤{C.RESET}")
    
    # Options
    for key, icon, label in options:
        key_str = f"[{key}]"
        line = f" {C.BCYAN}{C.BOLD}{key_str:>5}{C.RESET}  {icon}  {C.WHITE}{label}{C.RESET}"
        
        # Visible length calculation
        visible_len = 5 + 2 + len(icon) + 2 + len(label)
        spaces = width + 4 - visible_len - 1
        
        print(f"{C.BCYAN}{C.BOLD}    │{C.RESET}{line}{' ' * spaces}{C.BCYAN}{C.BOLD}│{C.RESET}")
    
    print(f"{C.BCYAN}{C.BOLD}    ╰{'─' * (width + 4)}╯{C.RESET}")
    print()


# ============================================================
# MESSAGES
# ============================================================
def print_success(msg):
    print(f"  {C.BGREEN}{C.BOLD}[+]{C.RESET} {C.GREEN}{msg}{C.RESET}")


def print_error(msg):
    print(f"  {C.BRED}{C.BOLD}[-]{C.RESET} {C.RED}{msg}{C.RESET}")


def print_warning(msg):
    print(f"  {C.BYELLOW}{C.BOLD}[!]{C.RESET} {C.YELLOW}{msg}{C.RESET}")


def print_info(msg):
    print(f"  {C.BBLUE}{C.BOLD}[*]{C.RESET} {C.BLUE}{msg}{C.RESET}")


def print_finding(title, severity, details=""):
    """Print a finding with severity color"""
    colors = {
        "CRITICAL": (C.BG_RED, C.BWHITE, "🔴"),
        "HIGH": (C.RED, C.BRED, "🟠"),
        "MEDIUM": (C.YELLOW, C.BYELLOW, "🟡"),
        "LOW": (C.BLUE, C.BBLUE, "🔵"),
        "INFO": (C.CYAN, C.BCYAN, "ℹ️"),
    }
    
    bg, fg, icon = colors.get(severity, (C.WHITE, C.BWHITE, "•"))
    
    print()
    print(f"  {bg}{C.BOLD} {severity} {C.RESET} {fg}{C.BOLD}{icon} {title}{C.RESET}")
    if details:
        for line in details.split('\n'):
            print(f"    {C.DIM}{line}{C.RESET}")


def print_section(title):
    """Print section header"""
    width = get_terminal_width()
    padding = (width - len(title) - 4) // 2
    
    print()
    print(f"{C.BCYAN}{'─' * width}{C.RESET}")
    print(f"{C.BCYAN}{'─' * padding}{C.RESET} {C.BOLD}{C.BWHITE}{title}{C.RESET} {C.BCYAN}{'─' * padding}{C.RESET}")
    print(f"{C.BCYAN}{'─' * width}{C.RESET}")
    print()


# ============================================================
# INPUT
# ============================================================
def ask(prompt, default=""):
    """Ask for input"""
    if default:
        prompt_str = f"  {C.BMAGENTA}{C.BOLD}?{C.RESET} {C.WHITE}{prompt}{C.RESET} {C.DIM}[{default}]{C.RESET}: "
    else:
        prompt_str = f"  {C.BMAGENTA}{C.BOLD}?{C.RESET} {C.WHITE}{prompt}{C.RESET}: "
    
    try:
        result = input(prompt_str).strip()
        return result if result else default
    except (KeyboardInterrupt, EOFError):
        print()
        return default


def ask_password(prompt):
    """Ask for password (hidden input)"""
    import getpass
    return getpass.getpass(f"  {C.BMAGENTA}{C.BOLD}?{C.RESET} {C.WHITE}{prompt}{C.RESET}: ")


def confirm(prompt):
    """Yes/No confirmation"""
    result = input(f"  {C.BYELLOW}{C.BOLD}?{C.RESET} {C.WHITE}{prompt}{C.RESET} {C.DIM}[y/N]{C.RESET}: ").strip().lower()
    return result in ['y', 'yes']


def pause():
    """Pause and wait for Enter"""
    print()
    input(f"  {C.DIM}Press Enter to continue...{C.RESET}")


# ============================================================
# TABLES
# ============================================================
def print_table(headers, rows, title="", color=C.CYAN):
    """Print a beautiful table"""
    # Calculate column widths
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            if i < len(widths):
                widths[i] = max(widths[i], len(str(cell)))
    
    # Title
    if title:
        total_width = sum(widths) + len(widths) * 3 + 1
        print()
        print(f"{color}{C.BOLD}  {title}{C.RESET}")
        print(f"{color}{'─' * total_width}{C.RESET}")
    
    # Headers
    header_line = f"{color}{C.BOLD}  "
    for i, h in enumerate(headers):
        header_line += f"{h:<{widths[i]}}  "
    header_line += C.RESET
    print(header_line)
    
    # Separator
    sep_line = f"{color}  "
    for w in widths:
        sep_line += "─" * (w + 2)
    sep_line += C.RESET
    print(sep_line)
    
    # Rows
    for row in rows:
        row_line = "  "
        for i, cell in enumerate(row):
            if i < len(widths):
                row_line += f"{str(cell):<{widths[i]}}  "
        print(row_line)
    
    print()


# ============================================================
# PROGRESS BAR
# ============================================================
def progress_bar(current, total, width=40, prefix="", suffix=""):
    """Draw a progress bar"""
    percent = current / total if total > 0 else 0
    filled = int(width * percent)
    
    bar = "█" * filled + "░" * (width - filled)
    
    # Color gradient
    if percent < 0.3:
        color = C.RED
    elif percent < 0.7:
        color = C.YELLOW
    else:
        color = C.GREEN
    
    line = f"\r  {prefix} {color}{bar}{C.RESET} {percent * 100:5.1f}% {suffix}"
    sys.stdout.write(line)
    sys.stdout.flush()
    
    if current >= total:
        print()


def spinner(text, duration=2):
    """Show a spinner animation"""
    frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    end_time = time.time() + duration
    i = 0
    
    hide_cursor()
    try:
        while time.time() < end_time:
            frame = frames[i % len(frames)]
            sys.stdout.write(f"\r  {C.BCYAN}{frame}{C.RESET} {C.WHITE}{text}{C.RESET}")
            sys.stdout.flush()
            time.sleep(0.1)
            i += 1
        sys.stdout.write(f"\r  {C.BGREEN}✓{C.RESET} {C.WHITE}{text}{C.RESET}\n")
    finally:
        show_cursor()


# ============================================================
# ANIMATIONS
# ============================================================
def typewriter(text, delay=0.03, color=C.WHITE):
    """Typewriter effect"""
    for char in text:
        sys.stdout.write(f"{color}{char}{C.RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()


def fade_in(text, delay=0.05):
    """Fade in effect"""
    for i in range(0, len(text), 5):
        sys.stdout.write(f"\r{C.WHITE}{text[:i]}{C.RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print(f"\r{C.WHITE}{text}{C.RESET}")


def matrix_rain(duration=3):
    """Matrix rain animation"""
    import random
    
    width = get_terminal_width()
    height = 20
    chars = "01アイウエオカキクケコサシスセソタチツテトナニヌネノ"
    
    # Initialize columns
    columns = [0] * width
    
    end_time = time.time() + duration
    hide_cursor()
    
    try:
        while time.time() < end_time:
            for x in range(width):
                if columns[x] == 0:
                    if random.random() < 0.02:
                        columns[x] = random.randint(1, height)
                
                if columns[x] > 0:
                    y = height - columns[x]
                    char = random.choice(chars)
                    sys.stdout.write(f"\033[{y};{x}H{C.BGREEN}{char}{C.RESET}")
                    columns[x] -= 1
            
            time.sleep(0.1)
        
        clear()
    finally:
        show_cursor()


# ============================================================
# TOOL STATUS
# ============================================================
def show_tool_status(available, missing):
    """Show system tools status"""
    print()
    print(f"{C.BCYAN}{C.BOLD}  ╭─ System Tools ─────────────────────────╮{C.RESET}")
    
    if available:
        avail_str = " ".join([f"{C.GREEN}✓ {t}{C.RESET}" for t in available[:8]])
        print(f"{C.BCYAN}  │{C.RESET} {avail_str}")
    
    if missing:
        miss_str = " ".join([f"{C.RED}✗ {t}{C.RESET}" for t, _ in missing[:8]])
        print(f"{C.BCYAN}  │{C.RESET} {miss_str}")
    
    print(f"{C.BCYAN}{C.BOLD}  ╰────────────────────────────────────────╯{C.RESET}")
    print()
