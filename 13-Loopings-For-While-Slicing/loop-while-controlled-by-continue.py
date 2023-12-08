from time import sleep

controller = 1

while True:
    sleep(1)
    print('The looping (while) is running.')
    if controller == 1:                                                      # Give a go, changing '1' to another value.
        continue               # it'll RESTART the loop with no reach the original lines next to the -continue- command.
    sleep(1)
    print('You will see this msg only cos -continue- has not been reached.')
    # break

sleep(1)
print('This message only will be shown if you included a -break- or a bool flag into the looping (while).')
