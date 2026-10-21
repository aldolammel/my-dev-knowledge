
Check if any users exist in the database:
```python
has_users = models.User.objects.exists()
```

Check if a specific user exists (filtering):
```python
email_taken = models.User.objects.filter(email="john@example.com").exists()
```

Check if a specific instance exists:
```python
is_alive = models.User.objects.filter(id=7).exists()
```

Check for active staff members:
```python
has_active_staff = models.User.objects.filter(is_staff=True, is_active=True).exists()
```

Check if a superuser does _not_ exist (setup check):
```python
needs_initial_setup = not models.User.objects.filter(is_superuser=True).exists()
```

