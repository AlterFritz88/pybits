PYBITES = "pybites"



def convert_pybites_chars(text):
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    text = text.split(" ")
    answer = []
    for word in text:
        temp = ""
        for char in word:
            if char in (PYBITES + PYBITES.upper()):
                temp += char.swapcase()
            else:
                temp += char
        answer.append(temp)

    return " ".join(answer)


text = "Today we added TWO NEW Bites to our Platform, exciting!"

print(convert_pybites_chars(text))