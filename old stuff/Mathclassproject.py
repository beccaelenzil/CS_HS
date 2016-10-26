import random
a = [0,11,[1/3,1/3,1/3],[1/3,1/3,1/3],[1/3,1/3,1/3],[1/3,1/3,1/3],[1/2,1/2],[1/2,1/2],[1/2,1/2],[1/2,1/2],[1/2,1/2],[1/2,1/2],[1/2,1/2],3,11,0]
b = [0,11,[1/3,1/3,1/3],[1/3,1/3,1/3],[1/3,1/3,1/3],[1/3,1/3,1/3],[1/2,1/2],[1/2,1/2],[1/2,1/2],[1/2,1/2],[1/2,1/2],[1/2,1/2],[1/2,1/2],3,11,0]
c = [0,11,[1/3,1/3,1/3],[1/3,1/3,1/3],[1/3,1/3,1/3],[1/3,1/3,1/3],[1/2,1/2],[1/2,1/2],[1/2,1/2],[1/2,1/2],[1/2,1/2],[1/2,1/2],[1/2,1/2],3,11,0]
'''
d = [1,2,[1/3,1/3,1/3],[1/3,1/3,1/3],[1/3,1/3,1/3],[1/3,1/3,1/3],[1/2,1/2],[1/2,1/2],[1/2,1/2],[1/2,1/2],[1/2,1/2],[1/2,1/2],[1/2,1/2],2,2,0]
e = [1,2,[1/3,1/3,1/3],[1/3,1/3,1/3],[1/3,1/3,1/3],[1/3,1/3,1/3],[1/2,1/2],[1/2,1/2],[1/2,1/2],[1/2,1/2],[1/2,1/2],[1/2,1/2],[1/2,1/2],2,2,0]
f = [2,5,[1/3,1/3,1/3],[1/3,1/3,1/3],[1/3,1/3,1/3],[1/3,1/3,1/3],[1/2,1/2],[1/2,1/2],[1/2,1/2],[1/2,1/2],[1/2,1/2],[1/2,1/2],[1/2,1/2],1,5,0]
'''
playerlist = [a,b,c]
def counttotals():
    totals = [0,0,0]
    for i in playerlist:
        if i[0] == 0:
            totals[0] = totals[0] + 1
        elif i[0] == 1:
            totals[1] = totals[1] + 1
        else:
            totals[2] = totals[2] + 1
    return totals
def chooseposition(player,totals):
    if player[0] == 1:
        if totals[1] == 1:
            player[1] = 1
        elif totals[1] == 3:
            player[1] = 4
        elif totals[0] == 2:
            player[1] = 3
        else:
            player[1] = 2
    elif totals[player[0]] == 1:
        if totals[1] == 2:
            player[1] = 5
        else:
            player[1] = 6
    elif totals[player[0]] == 3:
        if totals[1] == 1:
            player[1] = 10
        else:
            player[1] = 11
    elif totals[1] == 1:
        player[1] = 7
    elif totals[1] == 2:
        player[1] = 8
    else:
        player[1] = 9
def whereis():
    total1 = counttotals()
    if total1[0] == total1[1]:
        return 0
    else:
        start = 1
        total2 = [0,0,0]
        for g in total1:
            total2[g-1] = start
            start = start + 1
        return total2
def change(player,to,total2):
    player[-1] = to
    if to == 0:
        pass
    elif total2 == 0:
        if player[0] == 0 or player[0] == 2:
            player[0] = 1
        elif to == 1:
            player[0] = 0
        else:
            player[0] = 2
    elif to == 1:
        if player[1] in [2,4,7,10]:
            player[0] = total2[1]
        elif player[1] in [1,5,11]:
            player[0] = total2[2]
        else:
            player[0] = total2[3]
    elif player[1] == 4:
        player[0] = total2[2]
    else:
        player[0] = total2[3]

def execute(player,total2):
    integer = random.randint(0,1000000)
    if player[1] < 5:
        if integer < player[player[1]+1][0]*1000000:
            change(player,0,total2)
        elif integer > (1-player[player[1]+1][2])*1000000:
            change(player,2,total2)
        else:
            change(player,1,total2)
    else:
        lis = player[player[1]+1]
        if integer < lis[0]*1000000:
            change(player,0,total2)
        else:
            change(player,1,total2)
def readjust(player):
    improvement = player[0] - player[-3]
    if improvement == 2:
        if player[-2] < 5:
            improve1(player,5/3)
        else:
            improve2(player,5/3)
    elif improvement == 1:
        if player[-2] < 5:
            improve1(player,4/3)
        else:
            improve2(player,4/3)
    elif improvement == 0:
        pass
    elif improvement == -1:
        if player[-2] < 5:
            improve1(player,2/3)
        else:
            improve2(player,2/3)
    elif improvement == -2:
        if player[-2] < 5:
            improve1(player,1/3)
        else:
            improve2(player,1/3)
def improve1(player,multiplier):
    a = player[player[-2]+1][0]
    b = player[player[-2]+1][1]
    c = player[player[-2]+1][2]
    if player[-1] == 0:
        a = a*multiplier
        player[player[-2]+1] = [a,b+(1-a)*b/(b+c),c+(1-a)*c/(b+c)]
    if player[-1] == 1:
        b = b*multiplier
        player[player[-2]+1] = [a+(1-b)*a/(a+c),b,c+(1-b)*c/(a+c)]
    if player[-1] == 2:
        c = c*multiplier
        player[player[-2]+1] = [a+(1-c)*a/(a+b),b+(1-c)*b/(a+b),c]
def improve2(player,multiplier):
    a = player[player[-2]+1][0]
    b = player[player[-2]+1][0]
    if player[-1] == 0:
        a = a*multiplier
        player[player[-2]+1] = [a,b+b*(1-a)]
    else:
        b = b*multiplier
        player[player[-2]+1] = [a+a*(1-b),b]
def turn():
    global  a,b,c,d,e,f,playerlist
    total2 = whereis()
    for i in playerlist:
        chooseposition(i,counttotals())
    for i in playerlist:
       execute(i,total2)
    for i in playerlist:
        readjust(i)
        i[-1] = i[1]
        i[-2] = i[0]
def main():
    for i in range((10)):
        turn()
main()
print a
print b
print c
print d
print e
print f
