```python
is_authenticated = True
has_permission = True

if is_authenticated and has_permission:
    print("Access granted")

# Safe attribute/method access via short-circuiting
user = {"profile": {"name": "Ana"}}
name = user and user.get("profile", {}).get("name")  # "Ana"

empty_user = None
name = empty_user and empty_user["name"]  # None (right side isn't evaluated)
```
Value return and short-circuiting:
```python
10 and "hello"       # "hello" (both truthy -> returns last)
0 and "hello"        # 0       (0 is falsy -> stops and returns 0)
"" and [1, 2]        # ""      ("" is falsy -> stops and returns "")
"a" and "b" and "c"  # "c"
```
Chained comparisons using `and`:
```python
score = 85

# Idiomatic Python
if 70 <= score <= 100:
    print("Passing")

# Equivalent explicit `and`
if score >= 70 and score <= 100:
    print("Passing")
```