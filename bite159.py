def simple_calculator(calculation):
    """Receives 'calculation' and returns the calculated result,

       Examples - input -> output:
       '2 * 3' -> 6
       '2 + 6' -> 8

       Support +, -, * and /, use "true" division (so 2/3 is .66
       rather than 0)

       Make sure you convert both numbers to ints.
       If bad data is passed in, raise a ValueError.
    """
    operation_list = ('+', '-', '*', '/')
    calc_list = calculation.split(' ')


    try:
        op_1 = int(calc_list[0])
        op_2 = int(calc_list[2])
        sign = calc_list[1]

    except:
        raise ValueError

    if sign not in operation_list:
        raise ValueError

    if sign == '+':
        return op_1 + op_2
    if sign == '-':
        return op_1 -op_2
    if sign == '*':
        return op_1 * op_2
    else:
        try:
            return op_1 / op_2
        except:
            raise ValueError
print(simple_calculator('1 / 0'))