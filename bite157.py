from string import ascii_letters, punctuation
def filter_accents(text):
    """Return a sequence of accented characters found in
       the passed in text string
    """
    strange_list = []
    digits = '1234567890'
    for i in list(text.replace(' ', '')):
        if i not in ascii_letters and i not in punctuation and i not in digits:
            strange_list.append(i.lower())

    return sorted(set(strange_list))


text = """The 5 French accents;
     "The cédille (cedilla) Ç ...
     "The accent aigu (acute accent) é ...
     "The accent circonflexe (circumflex) â, ê, î, ô, û ...
     "The accent grave (grave accent) à, è, ù ...
     "The accent tréma (dieresis/umlaut) ë, ï, ü"""
print(filter_accents(text))