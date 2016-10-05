# python 2
#
# Name:
#
# Homework 2, Problem 1a and 1b
# slicing and indexing challenges: Lists and Strings
#

pi = [3,1,4,1,5,9]
e = [2,7,1]
h = 'harvey'
m = 'mudd'
c = 'college'
# Example problem (problem 0):
# Creating the list [2,5,9] from pi and e
answer0 = [ e[0] ] + pi[-2:]
print answer0
#Problem 1
#Creating the list [7,1] from pi and e
answer1 = e[1:]
print answer1
#Problem 2
#Creating the list [9,1,1] from pi and e
answer2 = [pi[-1]] + [e[-1]] + [e[-1]]
print answer2
#Problem 3
#Creating the list [1,4,1,5,9] from pi and e
answer3 = pi[1:]
print answer3
#Problem 4
#Creating the list [1,2,3,4,5] from pi and e
answer4 = e[-1:-4:-2] + pi[0:5:2]
print answer4
#Problem 5
# Creating the string 'heyyou'
answer5 = h[0] + h[4:] + h[-1] + c[1] + m[1]
print answer5
#Problem 6
#Create 'collude'
answer6 = c[0:4] + m[1:3] + c[-1]
print answer6
#Problem 7
#Create 'arveyudd'
answer7 = h[1:] + m[1:]
print answer7
#Problem 8
#Create 'hardeharharhar'
answer8 = h[0:3] + m[-1] + c[-1] + h[0:3] + h[0:3] + h[0:3]
print answer8
#Problem 9
#Create 'legomyego'
answer9 = c[3:6] + c[1] + m[0] + h[-1] + c[-3:-1] + c[1]
print answer9
#Problem 10
#Create 'clearcall'
answer10 = c[0:5:2] + h[1:3] + c[0] + h[1] + c[2:4]
print answer10
