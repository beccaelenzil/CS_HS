import random as rand
print "Welcome to Camel"
print "You have stolen a camel to make your way across the great Mobi desert."
print "The natives want their camel back and are chasing you down! Survive your"
print "desert trek and out run the natives."

done = False
miles_travelled = 0
thirst = 0
tire = 0
natives_travel = -20
drinks = 3

while done == False:
    nativesdist = miles_travelled - natives_travel
    print "A. Drink from your canteen."
    print "B. Ahead moderate speed."
    print "C. Ahead full speed."
    print "D. Stop for the night."
    print "E. Status check."
    print "Q. Quit."
    user_choice = raw_input("?")
    choice = user_choice.upper()
    if choice == "Q":
        done = True
    elif choice == "D":
        tire = 0
        print "The Camel is happy"
        natives_travel += rand.randint(7,11)
    elif choice == "C":
        dist = rand.randint(10,16)
        print "Travelled",dist,"miles"
        miles_travelled += dist
        thirst += 1
        tire += rand.randint(1,3)
        natives_travel += rand.randint(7,10)
    elif choice == "B":
        dist = rand.randint(5,12)
        print "Travelled",dist,"miles"
        miles_travelled += dist
        thirst += 1
        tire += 1
        natives_travel += rand.randint(7,10)
    elif choice == "A":
        if drinks > 0:
            thirst = 0
            drinks += -1
            natives_travel += rand.randint(7,10)
        else:
            print "Out of drinks"
    elif choice == "E":
        print "Miles traveled:",miles_travelled
        print "Drinks in canteen:", drinks
        print "The natives are",nativesdist,"miles behind you"
    if 6 >= thirst > 4:
        print "You are thirsty"
    elif thirst > 6:
        print "You died of thirst"
        done = True
        break
    if 8 >= tire > 5:
        print "Your camel is tired"
    elif tire > 8:
        print "Your camel died"
        done = True
        break
    nativesdist = miles_travelled - natives_travel
    if 15 >= nativesdist > 0:
        print "The natives are getting close"
    elif nativesdist <= 0:
        print "The natives caught up"
        done = True
        break
    elif miles_travelled >= 200:
        print "You crossed the desert. You win"
        done = True
        break
    if rand.randint(1,200) == 100:
        print "You found an oasis"
        thirst = 0
        drinks = 3
        tire = 0
