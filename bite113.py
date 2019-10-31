from string import ascii_letters, punctuation

def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    words = text.split()
    digits = '1234567890'
    non_a = []
    for word in words:
        for letter in word:
            if (letter not in ascii_letters) and (letter not in punctuation) and (letter not in digits):
                non_a.append(word)
                break
    return non_a

print(extract_non_ascii_words('Over \u0e55\u0e57 57 flavours'))