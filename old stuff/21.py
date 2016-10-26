import random
import time
counter = 21
def instructions():
    ####### tells instructions
    print 'Take turns with me counting down from 21'
    print 'You can subtract by 1,2, or 3 each turn'
    print 'Whoever makes the counter 0 wins'
def play():
    ####### Directs player to their turn or computer's turn depending on their choice
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
    playagain()
def playagain():
    ######## repeats game if player wants. resets counter
    global counter
    counter = 21
    again = raw_input('Wanna play again?')
    if again == 'yes':
        play()
    elif again == 'no':
        print 'aight'
    else:
        print 'Please enter yes or no.'
        playagain()

def yourturn():
    ######### asks user for choice, subtratcts from counter, passes turn to computer
    global counter
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
    ####### selects choice for computer, subtracts from counter, passes turn to player. If can, makes choice counter mod 4.
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
def main():
    #### organizes functions into game
    instructions()
    play()
main()
