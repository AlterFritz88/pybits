from itertools import islice



from  string import ascii_uppercase


let = ascii_uppercase

def sequence_generator():
    while 1:
        for i in range(0, 26):
            yield i+1
            yield let[i]



gen = sequence_generator()
for i in gen:
    print(i)

