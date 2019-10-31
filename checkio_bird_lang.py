VOWELS = "aeiouy"

def translate(phrase):
    answer = ''
    arr = []
    for i, char in enumerate(list(phrase)):
        if i == 0:
            if phrase[0] in VOWELS:

                arr.append(phrase[0])

            else:
                answer += char
            continue
        if char not in VOWELS:
            answer += char
            continue
        if phrase[i-1] not in VOWELS and phrase[i-1] != ' ':
            continue
        if char in VOWELS:
            arr.append(char)

            if len(arr) == 3:

                answer += arr[-1]
                arr = []
    return answer

if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")