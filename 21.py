import random
counter = 21
def play():
    playfirst = raw_input('Would you like to go first? (yes or no)')
    if playfirst == 'yes':
        yourturn()
    elif playfirst == 'no':
        myturn()
    else:
        print 'Please choose yes or no'

def yourturn():
    global counter
    global turn
    userchoice = 0
    print 'Counter is:', counter
    while userchoice not in range(1,4):
        userchoice = int(raw_input('By how much would you like to subtract? (1-3)'))
    counter = counter - userchoice
    if counter == 0:
        print 'Counter is', counter
        print 'You win'
    else:
        myturn()
def myturn():
    global counter
    print 'Counter is:', counter
    if counter%4 == 0:
        computerchoice = random.randint(1,3)
    else:
        computerchoice = counter%4
    print 'Computer chooses:', computerchoice
    counter = counter - computerchoice
    if counter == 0:
        print 'Counter is:', counter
        print 'I win'
    else:
        yourturn()
play()
