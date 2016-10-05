guesslist = []
import random
def main():
    play()
def play():
    number = random.randint(0,100)
    a = 1
    while a != 0:
        guess = (raw_input('Guess:'))
        try:
            guess = int(guess)
            guesslist.append(guess)
            if number == guess:
                a = 0
                print 'you win, you guessed:', guesslist
                print 'it took you this many tries', len(guesslist)
                return a
            else:
                if number < guess:
                    print 'Too high, try again'
                else:
                    print 'Too low, try again'
        except:
            print 'try an integer'
main()
