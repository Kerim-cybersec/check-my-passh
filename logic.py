import hashlib
import math
import secrets
import string
import os

class PasswordTool:
    def __init__(self, blacklist_path="blacklist.txt"):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.full_path = os.path.join(base_dir, blacklist_path)
        self.blacklist = []
        self.load_blacklist()

    def load_blacklist(self):
        try:
            if os.path.exists(self.full_path):
                with open(self.full_path, 'rb') as f:
                    content = f.read().decode('utf-8', errors='ignore')
                    self.blacklist = [line.strip() for line in content.splitlines() if line.strip()]
            else:
                self.blacklist = []
        except Exception as e:
            print(f"Error loading blacklist: {e}")

    def get_entropy(self, password):
        if not password: return 0
        charset = 0
        if any(c.islower() for c in password): charset += 26
        if any(c.isupper() for c in password): charset += 26
        if any(c.isdigit() for c in password): charset += 10
        if any(c in string.punctuation for c in password): charset += 32
        
        
        if charset == 0: charset = 32

        entropy = len(password) * math.log2(charset)
        return round(entropy, 2)

    def generate_secure(self, length=16):
        alphabet = string.ascii_letters + string.digits + string.punctuation
        return ''.join(secrets.choice(alphabet) for _ in range(length))

    def crack_hash(self, target_hash, algo, verbose=True):
        """For MD5, SHA-1, and SHA-256 cracking."""
        target_hash = target_hash.strip().lower()
        for plaintext in self.blacklist:
            clean_text = plaintext.strip()
            digest = hashlib.new(algo, clean_text.encode('utf-8', errors='ignore')).hexdigest()
            
            if verbose:
                print(f"[*] Comparing: {clean_text:15} | {algo.upper()} Digest: {digest[:20]}...")
            
            if digest == target_hash:
                return clean_text
        return None