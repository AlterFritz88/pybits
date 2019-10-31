def kaprekar_step(l):
    l1 = sorted(l)
    l2 = sorted(l, reverse=True)

    num1 = int(''.join([str(x) for x in l1]))
    num2 = int(''.join([str(x) for x in l2]))

    if num1 > num2:
        return num1 - num2
    else:
        return num2 - num1

def numerics(n):
    return [int(x) for x in str(n)]


def kaprekar_loop(n):
    if not kaprekar_check(n):
        print('Ошибка! На вход подано число {}, не удовлетворяющее условиям процесса Капрекара'.format(n))
        return None

    temp_arr = []
    while n not in (495, 6174,549945, 631764):
        print(n)
        n = numerics(n)
        n = kaprekar_step(n)
        if n in temp_arr:
            print('Следующее число - {}, кажется процесс зациклился...'.format(n))
            return None
        temp_arr.append(n)
    print(n)

def kaprekar_check(n):
    if len(str(n)) in (3, 4, 6) and n not in (100, 1000, 100000) and len(set(numerics(n))) != 1:
        return True
    else:
        return False

print(kaprekar_loop(103304))