import random
import time
import math
def rs():
    return random.choice([-1,1])
def rwPos(start,nsteps):
    '''returns position of a particle starting at start, and taking
    nsteps random steps in either direction. prints position after each step'''
    currentPosition = start
    for i in range(0,nsteps):
        currentPosition = currentPosition + rs()
        print 'current position is' + str(currentPosition)
    return currentPosition

def rwsteps(start,lo,hi):
    '''places particle and start, and has it take random steps
    until it gets above hi or below lo. Shows visual of it moving
    back and forth, and prints number of steps it took finish once finished'''
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
    '''returns position of a particle starting at start, and taking
    nsteps random steps in either direction'''
    currentPosition = start
    for i in range(0,nsteps):
        currentPosition = currentPosition + rs()
    return currentPosition

def ave_signed_displacement(numtrials,steps):
    '''return average displacement of particle taking 100
    steps in numtrials trials'''
    counter = 0
    for i in range(numtrials):
        a = rwPosPlain(0,steps)
        counter += math.sqrt(a**2)
    return counter/numtrials
def ave_squared_displacement(numtrials,steps):
    '''return average squared displacement of particle taking steps
    steps in numtrials trials'''
    counter = 0
    for i in range(numtrials):
        counter += float(rwPosPlain(0,steps)**2)
    return counter/numtrials
#print ave_signed_displacement(1000,200)
#print ave_squared_displacement(1000,200)
def avesignedave(numtrials):
    '''return a list of the average signed distance of every step value for the first numtrials
    multiples of 5'''
    list = []
    for i in range(numtrials):
        list.append([5*i,ave_signed_displacement(500,5*i)])
    return list
print avesignedave(30)
"""
   In order to compute the average signed displacement for
   a random walker after 100 random steps, I ran rwPosPlain
   a number of times, adding the total to a counter, and then
   dividing the counter by the number of trials at the end. I
   did the same thing with the average squared displacement.
    100 trials:
    ave_signed_displacement: 7.62, 9.2, 7.86
    ave_squared_displacement: 96.96,103.92,105.0
    After running 100 trials 1000 times:
    signed: 7.61
    squared: 96.316
    50 trials 1000 times:
    signed: 5.594
    squared 47.74
    200 trials 1000 times:
    signed: 10.85
    squared: 191.028
"""
