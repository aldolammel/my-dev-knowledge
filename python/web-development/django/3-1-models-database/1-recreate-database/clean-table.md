#### Python > Django:
# Clean a specific table:

---

To delete all data from a specific table:

Open the shell:        
```bash
python manage.py shell

>>> from <subapp_name>.models import <ClassName>
>>> <ClassName>.objects.all().delete()
```

Output will be the amount of data deleted in that table. 