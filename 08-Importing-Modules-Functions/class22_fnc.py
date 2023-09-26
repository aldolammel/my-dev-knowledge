def fnc_factorial(_num=0):
    _fact = 1
    for _i in range(1, _num + 1):
        _fact = _fact * _i
    return _fact


def fnc_double(_num=0, _format=False):
    _num = _num * 2
    if not _format:
        return _num
    else:
        return fnc_currency(_num)


def fnc_triple(_num=0, _format=False):
    _num = _num * 3
    if not _format:
        return _num
    else:
        return fnc_currency(_num)


def fnc_increase(_price=0, _percent=0, _format=False):
    _price = int(_price + ((_price / 100) * _percent))
    if not _format:
        return _price
    else:
        return fnc_currency(_price)


def fnc_half(_num=0, _format=False):
    _num = int(_num / 2)
    if not _format:
        return _num
    else:
        return fnc_currency(_num)


def fnc_currency(_price=0, _currency='R$'):
    return f'{_currency}{_price:.2f}'.replace('.', ',')


def fnc_resume(_price=0, _percent=0, _format=False):
    print(
        f'\nAnalysing the price: {fnc_currency(_price)}'
        f'\n{"- " * 18}'
        f'\nIts half: {fnc_half(_price, True):>20}'
        f'\nIts double: {fnc_double(_price, True):>19}'
        f'\nPlus {_percent}%: {fnc_increase(_price, _percent, True):>21}'
    )
