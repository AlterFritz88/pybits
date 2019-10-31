# nice snippet: https://gist.github.com/tonybruess/9405134
from collections import namedtuple
import re

social_platforms = """Twitter
  Min: 1
  Max: 15
  Can contain: a-z A-Z 0-9 _

Facebook
  Min: 5
  Max: 50
  Can contain: a-z A-Z 0-9 .

Reddit
  Min: 3
  Max: 20
  Can contain: a-z A-Z 0-9 _ -
"""

# note range is of type range and regex is a re.compile object
Validator = namedtuple('Validator', 'range regex')


def parse_social_platforms_string():
    """Convert the social_platforms string above into a dict where
       keys = social platformsname and values = validator namedtuples"""
    val_dict = {}
    for i in social_platforms.split('\n\n'):
        media = i.split('\n')

        range_val = range(int(media[1].strip().split(' ')[1]), int(media[2].strip().split(' ')[1])+1)
        reg_ex = '^[' + media[3].split(': ')[1].replace(' ', '') + ']+$'
        #re.compile("^([A-Z][0-9]
        val_dict[media[0]] = Validator(range_val, re.compile(reg_ex))
    return val_dict


def validate_username(platform, username):
    """Receives platforms(Twitter, Facebook or Reddit) and username string,
       raise a ValueError if the wrong platform is passed in,
       return True/False if username is valid for entered platform"""
    all_validators = parse_social_platforms_string()
    if platform not in all_validators.keys():
        raise ValueError
    if len(username) not in all_validators[platform].range:
        return False
    if all_validators[platform].regex.match(username) == None:
        return False
    return True

print(parse_social_platforms_string())

print(validate_username('Facebook', 'bobb,'))