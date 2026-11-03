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