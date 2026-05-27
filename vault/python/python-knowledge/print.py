# VARIABLE AND PRINT COMMAND'S BASIC:

name = 'Gordon Freeman'
print('It\'s a pleasure finally meet you,', name, '.')
print("It's a pleasure finally meet you,", name, ".")
print(f"It's a pleasure finally meet you, {name}.")

name = input("What's your name? ")
age = input('How old are you? ')
town = input('Where do you from? ')
day = input('Which day did you born? ')
month = input('Which month did you born? No numbers here, please! ')
year = input('Which year did you born? ')

print(name, ', ', age, ' from ', town, '.')
print('Hey ' + name + ', welcome!')
print('I see that you born in', month, day, 'of', year, '. That is true? Awesome!')
print()
print(
    '''Oh, just for we don\'t forget:\nIn this example, you may type an essay like
    this and, using three quotation marks, the text can be huge with no additional prints
    command at all.'''
)
print(
    """Oh, just for we don't forget:\nIn this example, you may type an essay like
    this and, using three quotation marks, the text can be huge with no additional prints
    command at all."""
)
