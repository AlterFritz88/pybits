def get_index_different_char(chars):
    alphanumeric = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    al_num = [x for x in list(enumerate(chars)) if str(x[1]) in alphanumeric and  x[1] != '']
    not_al_num = [x for x in list(enumerate(chars)) if str(x[1]) not in alphanumeric or x[1] == '']
    print(al_num)
    print(not_al_num)
    if al_num > not_al_num:
        return al_num[0][0]
    else:
        return not_al_num[0][0]

chars = ['=', '=', '', '/', '/', 9, ':', ';', '?', '¡']
print(get_index_different_char(chars))