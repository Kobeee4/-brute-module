import os
import sys
import random
from module import UniversalBruter

R = '\033[31m'
G = '\033[32m'
Y = '\033[33m'
B = '\033[34m'
C = '\033[36m'
W = '\033[0m'

def banner():
    os.system('clear')
    colors = [R, G, Y, B, C]
    clr = random.choice(colors)
    
    print(f"""{clr}
    
     █████╗ ██╗     ████████╗███████╗██████╗ ███╗   ██╗ █████╗ ████████╗██╗██╗   ██╗███████╗
    ██╔══██╗██║     ╚══██╔══╝██╔════╝██╔══██╗████╗  ██║██╔══██╗╚══██╔══╝██║██║   ██║██╔════╝
    ███████║██║        ██║   █████╗  ██████╔╝██╔██╗ ██║███████║   ██║   ██║██║   ██║█████╗  
    ██╔══██║██║        ██║   ██╔══╝  ██╔══██╗██║╚██╗██║██╔══██║   ██║   ██║╚██╗ ██╔╝██╔══╝  
    ██║  ██║███████╗   ██║   ███████╗██║  ██║██║ ╚████║██║  ██║   ██║   ██║ ╚████╔╝ ███████╗
    ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═══╝  ╚══════╝
                                                                                    
    {W}{Y}==============={W} {C}Un-Rooted Alternative To Hydra{W} {Y}================{W}
    {R}      [!] Warning: testing only | Unauthorized use is prohibited [!]{W}
    """)

def menu():
    banner()
    
    print(f"{G}[+]{W} Target Settings")
    target = input(f" └── {Y}URL:{W} ")
    user = input(f" └── {Y}Username:{W} ")
    u_field = input(f" └── {Y}User Field:{W} ")
    p_field = input(f" └── {Y}Pass Field:{W} ")
    fail = input(f" └── {Y}Failure String:{W} ")
    
    print(f"\n{G}[+]{W} Wordlist & Config")
    w_list = input(f" └── {Y}Path:{W} ")
    json_mode = input(f" └── {Y}Use JSON? (y/n):{W} ").lower() == 'y'
    
    print(f"\n{B}[*]{W} Initializing engine...")
    scanner = UniversalBruter(target, u_field, p_field, user, fail)
    
    try:
        with open(w_list, 'r', errors='ignore') as f:
            for i, line in enumerate(f):
                pwd = line.strip()
                sys.stdout.write(f"\r{C}[*]{W} Attempt {i+1}: {Y}{pwd[:15]}{W}...")
                sys.stdout.flush()
                
                res = scanner.attempt(pwd, use_json=json_mode)
                
                if res == "CAPTCHA":
                    print(f"\n{R}[!] Blocked by CAPTCHA at: {pwd}{W}")
                    return
                elif res is True:
                    print(f"\n\n{G}[SUCCESS]{W}")
                    print(f" └── {G}Password Found:{W} {pwd}")
                    return
        
        print(f"\n\n{R}[-]{W} Exhausted wordlist. No match.")
    except KeyboardInterrupt:
        print(f"\n\n{R}[!] Aborted.{W}")
    except Exception as e:
        print(f"\n{R}[ERROR]{W} {e}")

if __name__ == "__main__":
    menu()
