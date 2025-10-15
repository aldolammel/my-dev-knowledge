"""
    PYTHON: WHAT ARE PACKAGES AND MODULES AND HOW TO USE THEM

        PACKAGES VS MODULES:
            ./1-packages-vs-modules.txt

"""

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


