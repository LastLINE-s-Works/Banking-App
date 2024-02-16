def setuplogic():
    with open('setupkey','r') as f:
        validkey = f.read()
    getkey = input('Enter 22 Digit Setup Key: ')
    if getkey != validkey:
        print('Wrong Key!')