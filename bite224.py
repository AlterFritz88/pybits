import re

def get_sentences(text):
    """Return a list of sentences as extracted from the text passed in.
       A sentence starts with [A-Z] and ends with [.?!]"""
    pattern = re.compile(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s')
    return re.split(pattern, text.strip())

print(get_sentences("""We are looking forward attending the next Pycon in the U.S.A.
in 2020. Hope you do so too. There is no better Python networking
event than Pycon. Meet awesome people and get inspired. Btw this
dot (.) should not end this sentence, the next one should. Have fun!"""))