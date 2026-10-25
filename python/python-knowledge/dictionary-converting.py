
"""
    DICTIONARY > CONVERSION:
        xxxxxxxxxxxxxxxxxxx.

        >> List conversion:
            /python/python-knowledge/list-conversion.py

        >> Tuple conversion:
            /python/python-knowledge/tuple-conversion.py.py

"""

# Converting list or tuple to a dictionary:
lst = [('a', 1), ('b', 2)]
tpl = (('a', 1), ('b', 2))
tplst = (['a', 1], ['b', 2])

dict(lst)   # {'a': 1, 'b': 2}
dict(tpl)   # {'a': 1, 'b': 2}
dict(tplst) # {'a': 1, 'b': 2}