# Python Essential Training
# Module 11: File I/O
# Author: Dr. Alfred Ang
# Update: 19 Jan 2017


# Open a file to write or append
f = open('test.txt','w')

for i in range(10):
	f.write('Hello {}\n'.format(i+10))

f.close()

# f = open('test.txt','w')
f = open('test.txt','a')
f.write('Hello')
f.close()

# with open('test.txt','w') as f:
# 	for i in range(10):
# 		f.write('Test {}\n'.format(i))

# with open('test.txt','a') as f:
# 	for i in range(10):
# 		f.write('Test {}\n'.format(i+10))

#f.write('Test again')

# Open a file to read
# try:
# 	f = open('test.txt','r')
# except:
# 	print("check your file name")

# fl = f.readlines()

# for i in fl:
# 	print(i.strip())

# f.close()

# 2nd method: with open
# try:
# 	with open('test.txt','r') as f:
# 		for i in f:
# 			print(i.strip())
# except:
# 	print("check your file name")

# 3rd method: for open
# try:
# 	for i in open('test.txt','r'):
# 			print(i.strip())
# except:
# 	print("check your file name")


# Read CSV file
# import csv
# with open('test.csv', 'r') as f:
# 	fl = csv.reader(f)
# 	for i in fl:
# 		print(i)

# Challenge

import sqlite3

db = sqlite3.connect('school.db')

students = db.execute('select * from subjects order by subject')
print(students)
# for i in students:
# 	print(i)

f = open('subjects.txt','w')
for i,j,k in students:
    f.write("{}\t{}\t{}\n".format(i,j,k))
# for row in students:
#     f.write(str(row))
f.close()

with open('subjects.txt','w') as f:
	for i,j,k in students:
		f.write("{}\t{}\t{}\n".format(i,j,k))


f = open("subjects.txt","r")
for i in f:
    print(i.strip())
f.close()

f = open("subjects.txt","r")
f.readlines()
f.close()

f = open("subjects.txt","r")
f.readline()
f.close()

f = open("subjects.txt","r")
f.read()
f.close()

for i in open('subjects.txt','r'):
    print(i.strip())

f = open("python.txt","r")
paragraph = f.read()
f.close()
len(set(paragraph.split()))
