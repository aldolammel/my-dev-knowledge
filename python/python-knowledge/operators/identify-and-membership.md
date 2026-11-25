```python
a = [1, 2]
b = [1, 2]
c = a

a is b       # False (different objects in memory)
a is c       # True  (same object identity)
a is not b   # True

# Use `is` for None checks (PEP 8 standard)
value = None
value is None      # True

# Membership tests
2 in a             # True
"py" not in "python" # False
"key" in {"key": 1}  # True (checks dict keys)
```