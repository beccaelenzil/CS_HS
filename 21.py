import random
import time
counter = 21
def play():
    valid = 0
    while valid == 0:
        try:
            playfirst = raw_input('Would you like to go first? (yes or no)')
            if playfirst == 'yes':
                valid = 1
                yourturn()
            elif playfirst == 'no':
                valid = 1
                myturn()
            else:
                print 'Please choose yes or no'
        except:
            print 'Please choose yes or no'

def yourturn():
    global counter
    global turn
    userchoice = 0
    print 'Counter is:', counter
    time.sleep(1)
    while userchoice not in range(1,4):
        try:
            userchoice = int(raw_input('By how much would you like to subtract? (1-3)'))
        except:
            userchoice = 4
    counter = counter - userchoice
    time.sleep(1)
    if counter == 0:
        print 'Counter is', counter
        time.sleep(1)
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
    time.sleep(1)
    print 'Computer chooses:', computerchoice
    counter = counter - computerchoice
    if counter == 0:
        time.sleep(1)
        print 'Counter is:', counter
        time.sleep(1)
        print 'I win'
    else:
        yourturn()
play()
