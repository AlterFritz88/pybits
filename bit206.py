from  math import ceil
def check_split(item_total, tax_rate, tip, people):
    """Calculate check value and evenly split.

       :param item_total: str (e.g. '$8.68')
       :param tax_rate: str (e.g. '4.75%)
       :param tip: str (e.g. '10%')
       :param people: int (e.g. 3)

       :return: tuple of (grand_total: str, splits: list)
                e.g. ('$10.00', [3.34, 3.33, 3.33])
    """
    item_total = float(item_total[1:])
    tax_rate = float(tax_rate[:-1]) / 100
    tip = float(tip[:-1]) / 100

    total = item_total + (item_total * tax_rate)
    total_tips = (total * tip)
    total += total_tips
    total = round(total, 2)
    piesce = round(total / people, 2)
    ans = [total - (piesce * (people - 1))] + ([piesce] * (people - 1))

    return ('${:.2f}'.format(total), ans)

print(check_split('$100.03', '0%', '0%', 4))