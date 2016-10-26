import random
import time
def rs():
    return random.choice([-1,1])
def rwPos(start,nsteps):
    currentPosition = start
    for i in range(0,nsteps):
        currentPosition = currentPosition + rs()
        print 'current position is' + str(currentPosition)
    return currentPosition

def rwsteps(start,lo,hi):
    counter = 0
    currentPosition = start
    while currentPosition < hi and currentPosition > lo:
        time.sleep(.005)
        counter += 1
        startspace = ' '*(currentPosition-lo-1)
        endspace = ' '*(hi-currentPosition-1)
        print '|'+startspace+'S'+endspace+'|',currentPosition
        currentPosition += rs()
    print 'It took', counter,'times'

#rwsteps(75,0,150)

def rwPosPlain(start,nsteps):
    currentPosition = start
    for i in range(0,nsteps):
        currentPosition = currentPosition + rs()
    return currentPosition

def ave_signed_displacement(numtrials):
    counter = 0
    for i in range(numtrials):
        counter += rwPosPlain(0,100)
    return counter/numtrials
def ave_squared_displacement(numtrials):
    counter = 0
    for i in range(numtrials):
        counter += rwPosPlain(0,100)**2
    return counter/numtrials
print ave_signed_displacement(100)
print ave_squared_displacement(100)

"""
   In order to compute the average signed displacement for
   a random walker after 100 random steps, I ran rwPosPlain
   a number of times, adding the total to a counter, and then
   dividing the counter by the number of trials at the end. I
   did the same thing with the average squared displacement.

    ave_signed_displacement: 1, -1, -1
    ave_squared_displacement: 87,112,115
"""
