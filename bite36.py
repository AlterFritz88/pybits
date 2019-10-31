def get_profile(name, age, *args, **kwargs):
    if type(age) != int:
        raise ValueError
    if len(args) > 5:
        raise ValueError
    dic = {'name': name, 'age':age}
    if len(args) > 0:
        dic['sports'] = sorted([*args])
    if len(kwargs.keys()) > 0:
        dic['awards'] = kwargs
    return dic

print(get_profile('tim', 36, 'tennis', 'basketball',
                       service='going the extra mile for our customers',
                       champ='helped out the team in crisis',
                       attitude='unbeatable positive + uplifting'))