import random, string
def gen_key(parts, chars_per_part):

    return '-'.join([''.join(random.choices(string.ascii_uppercase + string.digits, k=chars_per_part)) for x in range(parts)])

print(gen_key(5,5))