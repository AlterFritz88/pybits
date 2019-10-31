COL_WIDTH = 20
import textwrap

def text_to_columns(text):
    """Split text (input arg) to columns, the amount of double
       newlines (\n\n) in text determines the amount of columns.
       Return a string with the column output like:
       line1\nline2\nline3\n ... etc ...
       See also the tests for more info."""

    senteses = [x.strip() for x in text.strip().split('\n\n')]
    dev_strings = []
    for sent in senteses:
        words = sent.split()
        strings = []
        while len(words) > 0:
            string = ''
            for i, word in enumerate(words):
                if len(string + ' ' + word) <= COL_WIDTH+1:
                    string += word + ' '
                else:
                    break
            strings.append(string + 5 * ' ')
            for d in string.split():
                words.remove(d)

        dev_strings.append(strings)
    dev_strings[-1] = [x.replace('      ', '\n') for x in dev_strings[-1]]
    max_sent = max([len(x) for x in dev_strings])
    final_sents = []
    for sent in  dev_strings:
        if len(sent) < max_sent:
            new_sent = sent[:]
            while len(new_sent) < max_sent:
                new_sent.append(' ' * 10)
            final_sents.append(new_sent)
        else:
            final_sents.append(sent)

    ans = ''
    for i, sent in enumerate(final_sents[0]):
        for q in final_sents:
            ans += q[i]

    return ans




text = """My house is small but cosy.

    It has a white kitchen and an empty fridge.

    I have a very comfortable couch, people love to sit on it."""

print(text_to_columns(text))