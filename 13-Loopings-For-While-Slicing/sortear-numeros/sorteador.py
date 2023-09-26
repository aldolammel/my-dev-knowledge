from time import sleep
from random import randint

debug = False
rounds_limit = 10  # number of available rounds to complete one unique prize draw!
rounds_done = 0
numbers_already_drawn = list()

while rounds_done < rounds_limit:
    drawn_number = randint(1, 60)  # pick up one of the available numbers.
    if drawn_number in numbers_already_drawn:
        if debug:
            print(f"SKIPPED! {drawn_number} was already drawn...")
        continue
    else:
        numbers_already_drawn.append(drawn_number)
        rounds_done += 1
        sleep(1)
        print(numbers_already_drawn)

sorted_numbers = sorted(numbers_already_drawn)
print(f"\n>> THE FINAL RESULT (WITH {len(numbers_already_drawn)} NUMBERS) IS: {sorted_numbers}\n\n")
