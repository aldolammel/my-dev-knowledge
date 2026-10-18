#### Python
# What are Packages and Modules

---
## PACKAGE
        
Package is a collection of multiple modules organized in a directory. So 'Packages' on Python is the same of 'libraries' in other languages!
- Must contain a special file called __init__.py (can be empty);
- Creates a namespace for related modules;

Structure, e.g.:
```python
my_package/             # <- This is the package
├── __init__.py         # <- Makes it a package
├── module1.py          # <- Module within the package
├── module2.py          # <- Another module
└── subpackage/         # <- Sub-package
	├── __init__.py
	└── module3.py
```

Real world examples:            
```python
import numpy            # Numerical computing package
import pandas           # Data analysis package  
import django           # Web framework package
import requests         # HTTP library package
```

---
## MODULE
        
A module is a single Python file (`.py`) that contains code - variables, functions, and classes that you can reuse.

Structure, e.g.:
`module4.py`  <---- Simple like this

Real world examples:
```python
import math             # Mathematical functions
import random           # Random number generation
import datetime         # Date and time utilities
```

---
## How to use them:
```python
# Import entire package:

import my_package
# Using it:
my_package.module1.some_function(...)


# Import specific module from package:
from my_package import module1
# Using it:
module1.some_function(...)


# Import specific function from package module:
from my_package.module1 import some_function
# Using it:
some_function(...)


# Import subpackage:
from my_package.subpackage import module3
# Using it:
module3.some_another_function(...)
```

---
## How to import things on Django:
[/python/web-development/django/3-1-models-database/importing-model-from-other-subapp](/python/web-development/django/3-1-models-database/importing-model-from-other-subapp.md)


