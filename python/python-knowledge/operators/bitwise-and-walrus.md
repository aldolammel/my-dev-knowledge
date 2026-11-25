```python
5 & 3      # 1  (bitwise AND)
5 | 3      # 7  (bitwise OR)
5 ^ 3      # 6  (bitwise XOR)
~5         # -6 (bitwise NOT: -(n + 1))
5 << 1     # 10 (left shift)
5 >> 1     # 2  (right shift)

# Walrus operator (assignment expression, Python 3.8+)
if (n := len(a)) > 1:
    print(f"List has {n} items")
```