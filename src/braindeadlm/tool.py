import subprocess
import os

def clear_screen_safe():
    command = 'cls' if os.name == 'nt' else 'clear'
    subprocess.run(command, shell=True)