```python
True and "ok"        # "ok"
False or "fallback"  # "fallback"
"" or "Guest"        # "Guest" (falsy values: False, None, 0, 0.0, "", [], {}, set())
not False            # True

# Ternary / conditional expression
status = "positive" if x > 0 else "non-positive"
```