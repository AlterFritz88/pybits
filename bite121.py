import re


def password_complexity(password):
    """Input: password string, calculate score according to 5 criteria in bite,
       return: score int"""
    score = 0
    if len(re.findall(r'[A-Z]', password)) > 0 and re.findall(r'[a-z]', password):
        score += 1
    if len(re.findall(r'[0-9]', password)) > 0 and (len(re.findall(r'[A-Z]', password)) > 0 or re.findall(r'[a-z]', password)):
        score += 1
    if len(re.findall(r'[@$]', password)) > 0:
        score += 1
    if len(password) >= 8:
        score += 1
    if len(password) >= 8 and len(re.findall(r'((.)\2{1,})', password)) == 0:
        score += 1
    print(re.search(r'[A-Z]+', password))
    return score


print(password_complexity('a1@1234'))