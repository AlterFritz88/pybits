def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    with open(file_, 'rb') as f:
        lines = f.read().decode("utf-8").split('\n')
        file = str(file_).split('/')[-1]
    count_line = str(len(lines))
    count_word = str(sum([len(x.split()) for x in lines]))
    count_chars = [x.split() for x in lines]
    chars = 0
    for i in count_chars:
        for word in i:
            print(word)
            for char in word:
                chars += 1
    return '\t' + count_line + '\t' + count_word + '\t' + str(chars + int(count_line) - 1 + int(count_word) - int(count_line)) + ' ' + file


