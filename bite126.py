import sys
import unicodedata


START_EMOJI_RANGE = 100000  # estimate


def what_means_emoji(emoji):
    """Receives emoji and returns its meaning,
       in case of a TypeError return 'Not found'"""
    try:
        return unicodedata.name(emoji)
    except TypeError:
        return 'Not found'
    except ValueError:
        return 'Not found'

def _make_emoji_mapping():
    """Helper to make a mapping of all possible emojis:
       - loop through range(START_EMOJI_RANGE, sys.maxunicode +1)
       - return dict with keys=emojis, values=names"""
    emoj_dict = {}
    for i in range(START_EMOJI_RANGE, sys.maxunicode +1):
        emoj_dict[chr(i)] = what_means_emoji(chr(i))
    return emoj_dict
    #print({k:v for k,v in emoj_dict.items() if v != 'Not found'})


def find_emoji(term):
    """Return emojis and their texts that match (case insensitive)
       term, print matches to console"""
    term = term.lower()

    emoji_mapping = _make_emoji_mapping()
    emoj = {}
    for k, v in emoji_mapping.items():
        if term in v.lower():
            emoj[k] = v
            print(v, k)
    print(emoj)
    if emoj == {}:
        print('no matches')


#print(what_means_emoji('aaa'))
#_make_emoji_mapping()
print(find_emoji('smiling'))