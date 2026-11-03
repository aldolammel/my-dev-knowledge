DICTIONARY > CONVERSION:

---

xxxxxxxxxxxxxxxxxxx.

List conversion:
/python/python-knowledge/list-conversion.py

Tuple conversion:
/python/python-knowledge/tuple-conversion.py.py
            
```python
# Converting list or tuple to a dictionary:
lst = [('a', 1), ('b', 2)]
tpl = (('a', 1), ('b', 2))
tplst = (['a', 1], ['b', 2])

dict(lst)   # {'a': 1, 'b': 2}
dict(tpl)   # {'a': 1, 'b': 2}
dict(tplst) # {'a': 1, 'b': 2}

```

---
## Unpacking different data types at the same time and together (flat)
```python
dict_ = {
	"a": 1,
	"b": 2,
}
list_ = [
	"a",
	"b",
]

all_of_them = [*dict_, *list_]  # It could be tuple, for example!
# output = ['a', 'b', 'a', 'b']
```
More about unpacking: [/python/python-knowledge/unpacking](/python/python-knowledge/unpacking.md)


