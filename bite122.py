def is_anagram(word1, word2):
    """Receives two words and returns True/False (boolean) if word2 is
       an anagram of word1, ignore case and spacing.
       About anagrams: https://en.wikipedia.org/wiki/Anagram"""
    letters_1 = sorted([x for x in word1.replace(' ', '')])
    letters_2 = sorted([x for x in word2.replace(' ', '')])
    return letters_1 == letters_2


#print(is_anagram("rail safety", "fairy fun"))


def double_letters(word):
    for i, let in enumerate(word[1:], 1):
        if let == word[i - 1]:
            return True
    return False

print(double_letters('koop'))


def comp(array1, array2):
    if type(array1) == None or type(array2) == None:
        return False
    if array1 == [] and array2 == []:
        return True
    try:
        return [x**2 for x in sorted(array1)] == [x for x in sorted(array2)]
    except:
        return False