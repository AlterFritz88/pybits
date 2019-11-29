import decimal


def check_split(item_total, tax_rate, tip, people):
    """Calculate check value and evenly split.

       :param item_total: str (e.g. '$8.68')
       :param tax_rate: str (e.g. '4.75%)
       :param tip: str (e.g. '10%')
       :param people: int (e.g. 3)

       :return: tuple of (grand_total: str, splits: list)
                e.g. ('$10.00', [3.34, 3.33, 3.33])
    """
    item_total = decimal.Decimal(float(item_total[1:]))
    tax_rate = decimal.Decimal(float(tax_rate[:-1]) / 100)
    tip = decimal.Decimal(float(tip[:-1]) / 100)

    total = item_total + (item_total * tax_rate)
    total = decimal.Decimal(total).quantize(decimal.Decimal('0.01'))
    total_tips = (total * tip)
    total += total_tips
    total = round(total, 2)
    piesce = round(total / people, 2)
    ans = [total - (piesce * (people - 1))] + ([piesce] * (people - 1))
    ans = [decimal.Decimal(x).quantize(decimal.Decimal('1.00')) for x in ans]

    return ('${:.2f}'.format(total), ans)

print(check_split('$191.57', '6.75%', '15%', 6))
grand_total, splits = check_split('$191.57', '6.75%', '15%', 6)
print(grand_total)
print(f'${sum(splits)}')