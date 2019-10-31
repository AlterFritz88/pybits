import string
import re

PUNCTUATION_CHARS = list(string.punctuation)


used_passwords = set('PassWord@1 PyBit$s9'.split())

def validate_password(password):
    digits = len(re.findall(r'\d', password)) > 0
    lenght = len(password) in range(6, 13)
    upper = len(re.findall(r'[A-Z]', password)) > 0
    lower = len(re.findall(r'[a-z]', password)) > 0
    no_used = password not in used_passwords
    punct = any(ext in password for ext in PUNCTUATION_CHARS)
    used_passwords.add(password)
    return digits and lenght and upper and lower and no_used and punct

print(validate_password('passWord9_'))
print(validate_password('passWord9_'))