#### Dev concepts
# Singleton

---

It's a design pattern that restricts the instantiation of a class to a single object and provides a global point of access to that instance.

---
## Key Characteristics:

- **Only one instance:** the class ensures that only one instance of itself is created;
- **Global access:** provides a way to access that single instance from anywhere in the app;
- **Controlled instantiation:** Prevents other objects from creating new instances.

---
## Why Use Singletons:

- **Shared resources:** when you need a single point of control (db connection, logger, configuration);
- **State management:** when you need to maintain global state across the app;
- **Performance:** avoid the overhead of creating multiple instances of expensive objects.

---
## Singleton Examples:

- In **Python**: [/python/web-development/django/3-1-models-database/singleton.py](/python/web-development/django/3-1-models-database/singleton.py)
- In **JavaScript**: /xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
