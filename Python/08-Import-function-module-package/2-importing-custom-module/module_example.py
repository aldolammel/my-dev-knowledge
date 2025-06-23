"""
MODULE EXAMPLE
Module names (file) the best practices ask to use all-lowercase and, if needed, underscore to separate words.
"""


def cal_factorial(n=0):
    fact = 1
    for _i in range(1, n + 1):
        fact = fact * _i
    return fact


def cal_double(n=0, format_=False):
    n = n * 2
    if not format_:
        return n
    else:
        return currency(n)


def cal_triple(n=0, format_=False):
    n = n * 3
    if not format_:
        return n
    else:
        return currency(n)


def cal_increase(price=0, percent=0, format_=False):
    price = int(price + ((price / 100) * percent))
    if not format_:
        return price
    else:
        return currency(price)


def cal_half(n=0, format_=False):
    n = int(n / 2)
    if not format_:
        return n
    else:
        return currency(n)


def currency(price=0, currency='R$'):
    return f'{currency}{price:.2f}'.replace('.', ',')


def resume(price=0, percent=0, format_=False):
    print(
        f'\nAnalysing the price: {currency(price)}'
        f'\n{"- " * 18}'
        f'\nIts half: {cal_half(price, True):>20}'
        f'\nIts double: {cal_double(price, True):>19}'
        f'\nPlus {percent}%: {cal_increase(price, percent, True):>21}'
    )
