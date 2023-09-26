"""

LIST COMPREHENSION with DICTIONARIES / DICTIONARY COMPREHENSION

At first:
WITH LIST OUTPUT: obj = [ comprehension syntax here ]
WITH DICTIONARY OUTPUT: obj = { comprehension syntax here } <-- Curly Brackets

SYNTAX EXAMPLE:
new_dictionary = { new_key: new_value FOR (key, value) IN original_dictionary.items() }

"""
from random import randint

print(">> CREATING A SIMPLE DICTIONARY AND PRINT IT OUT:")
friends = ['Rolf', 'Julie', 'Anton', 'Paul']
time_since_seen = [3, 6, 19, 23]
timer = {friends[i]: time_since_seen[i] for i in range(len(friends))}     # List comprehension with dict.
print(timer)

print('\n- - - -\n')

# ----------------------------------------------------------------------------------------------------------------------

print(">> CREATING A DICT OF STUDENTS' SCORE RANDOMLY AND, AFTER, SHOW ONLY THOSE WITH SCORE 6 OR HIGHER:")
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]  # Students
students_scores = {student: randint(1, 10) for student in names}    # Creating randomly the student's scores
print(students_scores)                                              # print it out to review
print('\nPassed students (score 6 or higher):')
passed_students = {student: score for (student, score) in students_scores.items() if score >= 6}
_ = [print(f'{key}: {value}') for (key, value) in passed_students.items()]

print('\n- - - -\n')

# ----------------------------------------------------------------------------------------------------------------------

print(">> CREATE A DICT WITH THE NUMBER OF LETTERS FROM EACH WORD PRESENTS IN THE SENTENCE BELOW:")
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
print(sentence)

result = {word: len(word) for word in sentence.split()}
print(result)

print('\n- - - -\n')

# ----------------------------------------------------------------------------------------------------------------------

print(">> CREATE A NEW DICT BY CONVERTING CELSIUS TO FAHRENHEIT TEMPERATURES:")
weather_c = {"Mon": 12, "Tue": 14, "Wed": 15, "Thu": 14, "Fri": 21, "Sat": 22, "Sun": 24}

# Traditional way to convert it:
"""weather_f = dict()
for (key, value) in weather_c.items():
    fahrenheit = (value * 9 / 5) + 32
    weather_f[key] = fahrenheit"""

# Dictionary comprehension method:
weather_f = {key: (value * 9 / 5) + 32 for (key, value) in weather_c.items()}

print(weather_f)

print('\n- - - -\n')

# ----------------------------------------------------------------------------------------------------------------------
