"""
-WHILE-, UNLIMITED LOOPING STRUCTURE (breaking with boolean):
(LAÇO DE REPETIÇÃO: WHILE)
"""

from time import sleep

isRunning = True

while isRunning:
    sleep(1)
    print('The looping (while) is running.')
    isRunning = False                           # it'll prevent the loop to run forever. Give a go, excluding this line.
    sleep(1)
    print('The looping (while) STILL running.')

sleep(1)
print('The looping (while) has been stopped coz "isRunning" got False in the middle of that looping.')
