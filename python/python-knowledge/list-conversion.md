```python
# ARRAY/LIST CONVERSION

# Converting a list to a tuple:
lst = [1,2,3,4]
tuple(lst) # Output: (1, 2, 3, 4)

# Converting a list to a dictionary:
#       /python/python-knowledge/dictionary-conversion.py
```

---
## Unpacking different data types at the same time and together (flat)
```python
tuple_ = (
	1,
	2,
)
list_ = [
	"a",
	"b",
]

all_of_them = [*tuple_, *list_]  # It could be tuple, for example!
# output = [1, 2, 'a', 'b']
```
More about unpacking: [/python/python-knowledge/unpacking](/python/python-knowledge/unpacking.md)

