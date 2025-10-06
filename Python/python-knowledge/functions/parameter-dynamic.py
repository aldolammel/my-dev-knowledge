
"""
    PYTHON: HOW TO MAKE A PARAMETER DYNAMIC

        You should use kwargs packing/unpacking:
            ../kwargs.py

        E.g.
            # The issue: that 'namefield' is part of a parameter. How to make that dynamic?
                
                if m.objects.filter(namefield__iexact="some_value"):
                    ...
"""

# Solution:
def check_char_case_sensitivity(field_name: str, field_value: str)

    # Creating the dynamic param and its value:
    dynamic_param = { f'{field_name}__iexact': field_value}  # always as a DICT.
    
    # Unpacking the dict to create a queryset to searching in the db, for example:
    qs = m.objects.filter(**dynamic_param):  # Equivalent: m.objects.filter(param=arg)
    
    ...


# Calling:
check_char_case_sensitivity("town", "Poa")  # Equivalent: m.objects.filter(town__iexact='Poa')

