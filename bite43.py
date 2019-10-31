def get_profile(*, name: str = 'julian', profession: str = 'programmer') -> str:
    return '{} is a {}'.format(name, profession)

print(get_profile(name='fff'))
get_profile('julian')