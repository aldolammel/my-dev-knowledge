"""
MODULE EXAMPLE
Module names (file) the best practices ask to use all-lowercase and, if needed, underscore to separate words.
"""


def cal_factorial(_num=0):
    _fact = 1
    for _i in range(1, _num + 1):
        _fact = _fact * _i
    return _fact


def cal_double(_num=0, _format=False):
    _num = _num * 2
    if not _format:
        return _num
    else:
        return currency(_num)


def cal_triple(_num=0, _format=False):
    _num = _num * 3
    if not _format:
        return _num
    else:
        return currency(_num)


def cal_increase(_price=0, _percent=0, _format=False):
    _price = int(_price + ((_price / 100) * _percent))
    if not _format:
        return _price
    else:
        return currency(_price)


def cal_half(_num=0, _format=False):
    _num = int(_num / 2)
    if not _format:
        return _num
    else:
        return currency(_num)


def currency(_price=0, _currency='R$'):
    return f'{_currency}{_price:.2f}'.replace('.', ',')


def resume(_price=0, _percent=0, _format=False):
    print(
        f'\nAnalysing the price: {currency(_price)}'
        f'\n{"- " * 18}'
        f'\nIts half: {cal_half(_price, True):>20}'
        f'\nIts double: {cal_double(_price, True):>19}'
        f'\nPlus {_percent}%: {cal_increase(_price, _percent, True):>21}'
    )
