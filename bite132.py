
VOWELS = list('aeiou')


def get_word_max_vowels(text):
    """Get the case insensitive word in text that has most vowels.
       Return a tuple of the matching word and the vowel count, e.g.
       ('object-oriented', 6)"""
    text_sp = text.split(' ')
    dic = {}
    for word in text_sp:
        count = 0
        for let in word:
            if let in VOWELS:
                count += 1
        dic[word] = count

    dic_sorted = sorted(dic.items(), key = lambda x: x[1])
    return dic_sorted[-1]

text = ("Python is an easy to learn, powerful programming language."
     "It has efficient high-level data structures and a simple "
     "but effective approach to object-oriented programming. "
     "Python’s elegant syntax and dynamic typing, together with "
     "its interpreted nature, make it an ideal language for "
     "scripting and rapid application development in many areas "
     "on most platforms.")

print(get_word_max_vowels(text))