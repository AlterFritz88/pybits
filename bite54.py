INDENTS = 4


def print_hanging_indents(poem):
    poem = poem.split('\n')
    poem = [x.strip() for x in poem]
    for i in range(len(poem)):
        if i == 0:
            print(poem[i])
            continue
        if i > 0 and poem[i] == '':
            continue
        if poem[i - 1] == '':
            print(poem[i])
        else:
            print(' '*INDENTS + poem[i])




shakespeare_unformatted = """
                          To be, or not to be, that is the question:
                          Whether 'tis nobler in the mind to suffer

                          The slings and arrows of outrageous fortune,
                          Or to take Arms against a Sea of troubles,
                          """

print(print_hanging_indents(shakespeare_unformatted))