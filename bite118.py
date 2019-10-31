def get_duplicate_indices(words):
    """Given a list of words, loop through the words and check for each
       word if it occurs more than once.
       If so return the index of its first ocurrence.
       For example in the following list 'is' and 'it'
       occurr more than once, and they are at indices 0 and 1 so you would
       return [0, 1]:
       ['is', 'it', 'true', 'or', 'is', 'it', 'not?'] => [0, 1]
       Make sure the returning list is unique and sorted in ascending order."""
    filtered = []
    score = []
    for word in words:
        if word in filtered:
            score.append(words.index(word))
        filtered.append(word)
    return list(set(score))



print(get_duplicate_indices(['this', 'is', 'a', 'new', 'bite', 'I', 'hope', 'this', 'bite', 'will', 'teach', 'you', 'something', 'new']))