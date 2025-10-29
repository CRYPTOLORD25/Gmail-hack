#!/bin/bash

# Gmail Cracker Installer for Linux/Mac
# Built by Crypto Lord

echo -e "\033[95m"
echo "╔══════════════════════════════════════════════════╗"
echo "║              GMAIL CRACKER INSTALLER             ║"
echo "║                 Built by Crypto Lord             ║"
echo "╚══════════════════════════════════════════════════╝"
echo -e "\033[0m"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo -e "\033[91m[ERROR] Python3 is not installed!\033[0m"
    echo "Please install Python3 from https://python.org"
    exit 1
fi

echo -e "\033[92m[✓] Python3 is installed\033[0m"

# Create virtual environment
echo -e "\033[93m[*] Creating virtual environment...\033[0m"
python3 -m venv gmail-hack_env

# Activate virtual environment
echo -e "\033[93m[*] Activating virtual environment...\033[0m"
source gmail-hack_env/bin/activate

# Install requirements
echo -e "\033[93m[*] Installing dependencies...\033[0m"
pip install --upgrade pip

# Create common passwords file
echo -e "\033[93m[*] Creating common passwords wordlist...\033[0m"
cat > rockyou.txt << EOL
password
123456
12345678
1234
12345
qwerty
password1
1234567
123456789
letmein
admin
welcome
monkey
abc123
password123
hello
shadow
master
dragon
baseball
football
EOL

# Make script executable
echo -e "\033[93m[*] Making script executable...\033[0m"
chmod +x gmail_cracker.py

echo -e "\033[92m"
echo "╔══════════════════════════════════════════════════╗"
echo "║                  INSTALLATION COMPLETE!          ║"
echo "╚══════════════════════════════════════════════════╝"
echo -e "\033[0m"

echo -e "\033[96m"
echo "To run the tool:"
echo "1. Activate environment: source gmail-hack_env/bin/activate"
echo "2. Run tool: python3 gmail_cracker.py"
echo ""
echo "Or use the provided run script: ./run.sh"
echo -e "\033[0m"

# Create run script
cat > run.sh << EOL
#!/bin/bash
source gmail-hack_env/bin/activate
python3 gmail_cracker.py "\$@"
EOL

chmod +x run.sh

echo -e "\033[92m[✓] Installation completed successfully!\033[0m"
echo -e "\033[93m[!] Remember: Use only for educational purposes!\033[0m"