#### Python > Django > Models > Attribute types
# FloatField()

---

Scientific calculations or measurements where speed is critical and small rounding errors are acceptable. Not suitable for financial data due to potential precision errors (e.g., 0.1 + 0.2 might not exactly equal 0.3). For storing numbers with decimal points, like *DecimalField*, but with differences!!! Double-precision floating-point.

Typical Size:
8 bytes (64-bit)

Signed Range:
Approximately ±1.7e±308 (with about 15-16 digits of precision)

E.g.
xxxxxxxxxxxxxxxxxx

---

## Other related options:
- DecimalField: [/python/web-development/django/3-1-models-database/model-attr-field-decimal](/python/web-development/django/3-1-models-database/model-attr-field-decimal.md)
