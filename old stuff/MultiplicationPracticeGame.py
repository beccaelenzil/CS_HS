def main():
    instructions()
    dif()
def instructions():
    print 'I give numbers, you multiply'
def dif():
    print 'pick a level between 1 and 5:'
    diffy = int(raw_input())
    play(diffy)
def play(d):
    import random
    for i in range(5):
        factor1 = random.randint(0,d)
        factor2 = random.randint(0,d)
        answer = factor1*factor2
        userAnswer = 'start'
        while userAnswer != answer:
            userAnswer = raw_input(str(factor1)+'*'+str(factor2)+'=')
            userAnswer = int(userAnswer)
            if userAnswer == answer:
                print 'good, again'
            else:
                print 'bad, again'
    print 'good'
main()
