import os
import urllib.request

LOG = os.path.join('temp', 'safari.logs')
PY_BOOK, OTHER_BOOK = 'py🐍🐍🐍', '.'
urllib.request.urlretrieve('http://bit.ly/2BLsCYc', LOG)


def create_chart():
    dates_dic  = {}
    with open(LOG, 'r') as f:
        list_log = f.read().split('\n')
    for i, log in enumerate(list_log):
        if log.split('-')[-1] == ' sending to slack channel':
            if 'Python' in list_log[i-1].split('- ')[-1]:
                char = PY_BOOK
            else:
                char = OTHER_BOOK
            if log.split(' ')[0] not in dates_dic.keys():
                dates_dic[log.split(' ')[0]] = [char]
            else:
                dates_dic[log.split(' ')[0]].append(char)
    for k, v in dates_dic.items():
        print('{} {}'.format(k, ''.join(v)))


print(create_chart())