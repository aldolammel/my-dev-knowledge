def calc_factorial(_num=0):
    _fact = 1
    for _i in range(1, _num + 1):
        _fact = _fact * _i
    return _fact


def calc_double(_num=0, _format=False):
    _num = _num * 2
    if not _format:
        return _num
    else:
        return currency(_num)


def calc_triple(_num=0, _format=False):
    _num = _num * 3
    if not _format:
        return _num
    else:
        return currency(_num)


def calc_increase(_price=0, _percent=0, _format=False):
    _price = int(_price + ((_price / 100) * _percent))
    if not _format:
        return _price
    else:
        return currency(_price)


def calc_half(_num=0, _format=False):
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
        f'\nIts half: {calc_half(_price, True):>20}'
        f'\nIts double: {calc_double(_price, True):>19}'
        f'\nPlus {_percent}%: {calc_increase(_price, _percent, True):>21}'
    )
