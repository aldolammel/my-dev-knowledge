```python
is_admin = False
is_staff = True

if is_admin or is_staff:
    print("Access granted")

# Default fallback when a value might be falsy (None, "", 0, [], {})
username = ""
display_name = username or "Anonymous"  # "Anonymous"

config_timeout = None
timeout = config_timeout or 30         # 30
```
Value Return & Short-Circuiting:
```python
False or "hello"      # "hello" (first truthy)
"first" or "second"   # "first" (stops at first truthy; "second" isn't evaluated)
0 or "" or []         # []      (all falsy -> returns last operand)
```
Bitwise / Set `|` vs. Logical `or`:
```python
# Bitwise OR on integers
0b1100 | 0b1010 == 0b1110  # True (12 | 10 == 14)

# Union on sets
{"read"} | {"write"}         # {"read", "write"}
```