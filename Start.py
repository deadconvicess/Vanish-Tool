# This is a Simple Python Script To Install What Vanish Needs.
# Vanish Was Coded by @deadconvicess 

import os
import subprocess
import sys
libraries = [
    "requests",
    "colorama",
    "pyfiglet",
    "termcolor",
    "tqdm",
    "httpx",
    "pillow",
    "keyboard",
    "beautifulsoup4",
    "lxml"
]

def install_libraries():
    print("Installing required Python libraries.\n")
    for lib in libraries:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
        except subprocess.CalledProcessError:
            print(f"Failed to install: {lib}")
            
def run_vanish():
    vanish_file = "Vanish.exe"
    if os.path.exists(vanish_file):
        subprocess.call([sys.executable, vanish_file])
    else:
        print(f"Vanish Not Found.")

if __name__ == "__main__":
    install_libraries()
    run_vanish()
