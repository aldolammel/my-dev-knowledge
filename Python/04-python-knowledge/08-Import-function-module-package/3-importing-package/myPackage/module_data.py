# MY COLORS
_corT = '\033[1;32m'
_corF = '\033[1;31m'
_corO = '\033[m'


def money_read(_msg):
    while True:
        _input = str(input(_msg)).replace(',', '.').strip()
        if _input.isalpha() or _input == '':
            print(f'{_corF}Error: "{_input}" is not a real price!{_corO}')
        else:
            break
    return float(_input)
