#### Python > Function
# `getattr()`

---

The `getattr()` is a Python built-in function that's used to retrieve the value of an object's attribute dynamically by passing its name as a string.
If the attribute doesn't exist, it can return an optional default value instead of raising an error.

E.g, `getattr(obj, 'attribute_name')

**So, it does:**
- Dynamic access: Retrieves an object's attribute using a string name.
- Safe fallback: Returns an optional default value instead of raising an `AttributeError` if the attribute doesn't exist.

---
## Common example:
```python
class Car:
    def __init__(self, brand):
        self.brand = brand

my_car = Car("Toyota")

# Access an existing attribute using its string name
getattr(my_car, 'brand')
# Output: Toyota

# Use a default value if the attribute doesn't exist (avoids AttributeError)
getattr(my_car, 'year', 2026)
# Output: 2026
```

---


