from time import sleep

while True:
    sleep(1)
    print('The looping (while) is running.')
    break   # it'll STOP immediately the loop. Give a go, excluding this line.
    sleep(1)
    print('The looping (while) STILL running.')  # With the -break- above, you won't see this message at all.

sleep(1)
print('The looping (while) has been stopped immediately coz "break" was called.')
