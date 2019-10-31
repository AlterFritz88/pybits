from copy import deepcopy
items = [{'id': 1, 'name': 'laptop', 'value': 1000},
         {'id': 2, 'name': 'chair', 'value': 300},
         {'id': 3, 'name': 'book', 'value': 20}]


def duplicate_items(items):
    return deepcopy(items)

new_item = duplicate_items(items)
new_item[0]['id'] = 88

print(items)