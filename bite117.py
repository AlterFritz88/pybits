from decimal import Decimal, ROUND_HALF_EVEN


def round_even(number):
    """Takes a number and returns it rounded even"""
    num = Decimal(number)
    return num.quantize(Decimal("1."), ROUND_HALF_EVEN)

    print(num)

round_even(1.6)