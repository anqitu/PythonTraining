# Python Essential Training
# Module 10: Exceptions
# Author: Dr. Alfred Ang
# Update: 19 Jan 2017

# index error
a = [1,2,3]
a[4]

# Simulate a error
# int('1')
# int('hello')
# a = int(input('Enter an integer : '))
# print("You enter ",a)

try:
	a = int(input('Enter an integer : '))
	print("You enter ", a)
except:
	print("Please enter an integer")


# f = open('test888.txt','r')

try:
    f = open('test888.txt', 'r')
except:
    print("file does not exist")

'hello'.endswith('ol')

def readfile(file):
    if(file.endswith('.txt')):
        f = open(file)
        return f.readlines()
    else:
        raise ValueError("wrong extension")

readfile('test')

try:
    readfile('test')
except ValueError as e:
    print(e)


# Challenge
import random

die = random.choice([1,2,3,4,5,6])
print('The correct answer is ',die)

while True:
	try:
		guess = int(input('Guess the die no : '))
		if guess == die:
			print("Good Guess")
			break
		else:
			int('wrong guess')
	except:
		print("Pls try again")

# 'a' > 0
int('a')
input = [1,2,3,"a",4,5,"b",6,7,"c"]
output = []
for i in input:
    try:
        output.append(int(i))
    except:
        pass
output
