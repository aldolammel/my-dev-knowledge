from time import time, sleep

# User definition:
secs_limit = 10

# Initial values:
elapsed_time = 0

# Constants:
START_TIME = time()

# Stopwatch check looping:
while elapsed_time < secs_limit:
    elapsed_time = time() - START_TIME
    print(f"Elapsed time = {elapsed_time:.1f}secs")
    sleep(0.1)
print(f"\n>> Stopwatch has been finished when {elapsed_time:.1f} secs was reached!\n")
