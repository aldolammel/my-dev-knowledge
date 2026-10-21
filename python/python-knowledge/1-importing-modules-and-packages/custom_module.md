#### Python > Importing modules and packages
# Custom module

---
## Before:
- How packages and modules work: [/python/python-knowledge/1-importing-modules-and-packages/1-packages-vs-modules](/python/python-knowledge/1-importing-modules-and-packages/1-packages-vs-modules.md)

---

Module names (file) the best practices ask to use all-lowercase and, if needed, underscore to separate words. So the filename should be snake_case!

File: `custom_module.py`
```python
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

```
## MODULE AND PACKAGE:
Packages on Python is the same of libraries in other languages.
```python
import custom_module  # importing functions from custom_module.py file!

# Pre-lessons:
user_n = int(input('Type an integer: '))
factorial = module_example.cal_factorial(user_n)

print(
	f'The factorial of {user_n} is: {factorial}'
	f'\nThe double of {user_n} is: {module_example.cal_double(user_n)}'
	f'\nThe triple of {user_n} is: {module_example.cal_triple(user_n)}'
)

# ----------------------------------------

user_p = float(input('Type a price: R$'))
module_example.resume(user_p, 30)
```

