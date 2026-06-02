#### Python > Django > Models > Attribute types
# SmallAutoField()

---

It's the small integer version of an auto-incrementing primary key. Automatically incrementing primary keys for small tables with a hard, known upper size limit. This is a very specific optimization tool.

Typical Size:
2 bytes (16-bit)

Signed Range:
1 to 32,767 (It's effectively unsigned and starts at 1, like other auto fields).

E.g.
```
id = models.SmallAutoField(
	primary_key=True,
	unique=True,
	editable=False,
)
```

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

>> Other related options:

    >> Auto Field:
        ./model-attr-field-auto.txt

    >> Big Auto Field:
        ./model-attr-field-bigAuto.txt




    