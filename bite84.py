

def flatten(list_of_lists):
    main_list = []
    def flat(list_of_lists):
        for i in list_of_lists:
            if type(i) not in (list, tuple):
                main_list.append(i)
            else:
                flat(i)
    flat(list_of_lists)
    return main_list


print(flatten([1, [2, 3], [4, 5, [6, 7, [8, 9, 10]]]]))



