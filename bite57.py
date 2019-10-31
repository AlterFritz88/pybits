import argparse

def calculator(operation, numbers):
    """TODO 1:
       Create a calculator that takes an operation and list of numbers.
       Perform the operation returning the result rounded to 2 decimals"""
    numbers = [float(x) for x in numbers]
    if operation.upper() == 'ADD':
        return round(sum(numbers), 2)
    if operation.upper() == 'SUB':
        return round(numbers[0] - sum(numbers[1:]), 2)
    if operation.upper() == 'MUL':
        mul = 1
        for item in numbers:
            mul *= item
        return round(mul, 2)
    if operation.upper() == 'DIV':
        div = numbers[0]
        for item in numbers[1:]:
            div /= item

        return round(div ,2)

def create_parser():
    """TODO 2:
       Create an ArgumentParser object:
       - have one operation argument,
       - have one or more integers that can be operated on.
       Returns a argparse.ArgumentParser object.

       Note that type=float times out here so do the casting in the calculator
       function above!"""
    parser = argparse.ArgumentParser(description='A simple calculator')

    parser.add_argument('-a', '--ADD', nargs='+',  required=False, help='Sums numbers')
    parser.add_argument('-s', '--SUB', nargs='+',  required=False, help='Subtracts numbers')
    parser.add_argument('-m', '--MUL', nargs='+',  required=False, help='Multiplies numbers')
    parser.add_argument('-d', '--DIV', nargs='+',  required=False, help='Divides numbers')
    return parser


def call_calculator(args=None, stdout=False):
    """Provided/done:
       Calls calculator with provided args object.
       If args are not provided get them via create_parser,
       if stdout is True print the result"""
    parser = create_parser()

    if args is None:
        args = parser.parse_args()


    # taking the first operation in args namespace
    # if combo, e.g. -a and -s, take the first one
    for operation, numbers in vars(args).items():

        if numbers is None:
            continue

        try:
            res = calculator(operation, numbers)
        except ZeroDivisionError:
            res = 0

        if stdout:
            print(res)

        return res


if __name__ == '__main__':
    call_calculator(stdout=True)