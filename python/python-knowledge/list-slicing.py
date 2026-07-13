# Lists (Mutable sequences)
my_list = [10, 20, 30, 40, 50]
print(my_list[1:4])      # Output: [20, 30, 40]


# General e.g.
phrase = 'Who is the Russian dwarf most famous nowadays?'

# Using slicing from 11th to the last phrase char:
phrase[11:]  # Output: 'Russian dwarf most famous nowadays?'

# From the phrase beginning to its 23rd letter:
phrase[:24]  # Output: 'Who is the Russian dwarf'

# From 11th to the 23rd (always one before) phrase letter:
phrase[11:24]  # Output: 'Russian dwarf'

# From the first til the last letter but jumping 3 and 3 letters:
phrase[::3]  # Output: 'xxxx'

# From the last til the first (reverse):
phrase[::-1]  # Output: '?syadawon suomaf tsom frawd naissuR eht si ohW'

# From the last til 9th char (not index), taking 'nowadays?' (reverse):
phrase[-9:]  # Output: 'xxxxxxxxx'
