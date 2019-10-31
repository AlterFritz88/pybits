punct = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    for char in punct:
        if char in input_string:
            input_string = input_string.replace(char, '')
    return input_string

print(remove_punctuation('Hello, I am Tim.'))