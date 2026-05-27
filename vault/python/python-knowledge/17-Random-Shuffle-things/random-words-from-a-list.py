from random import sample, shuffle


# Small amount of words from a list with unlimited amount:
print("\n>> Small amount of words from a list with unlimited amount:")
words_list = ["that", "with", "from", "this", "they", "will", "would", "about", "their", "there", "what", "which"]
print(f"Before: {words_list}")
words_new_list = sample(words_list, 3)
print(f"After: {words_new_list}")


# Shuffle all values in a list:
print("\n>> Shuffle all values in a list:")
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Before: {num_list}")
shuffle(num_list)  # Important: shuffle method modify the original list, so it can't be called during its action.
print(f"After: {num_list}")


