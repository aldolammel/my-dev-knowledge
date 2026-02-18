
"""
    PYTHON BUILT-IN METHOD: .COUNT()

        Be aware:
            This is not like the built-in function len():
                ./len-length.py

        
        Purpose:
            Counts occurrences of a specific element/value

        Works with:
            Specific sequence types (strings, lists, tuples)

        Performance:
            O(n) - linear time (must scan entire sequence)

        Syntax:
            sequence.count(element)
"""

# count() - specific character occurrences
print(text.count('l'))  # Output: 3
print(text.count('o'))  # Output: 2

# count() - occurrences of specific value
print(numbers.count(2))  # Output: 3
print(numbers.count(9))  # Output: 0 (not found)

# Comparison with len() function:
fruits = ('apple', 'banana', 'apple', 'orange')
print(len(fruits))        # Output: 4 (total items)
print(fruits.count('apple'))  # Output: 2 (occurrences)

