# Python Essential Training
# Module 9: Database
# Author: Dr. Alfred Ang
# Update: 19 Jan 2017

import sqlite3

db = sqlite3.connect('test.db')

db.execute('create table student (name text,rank int)')
db.commit()

# Insert Record
db.execute('insert into student (name,rank) values (?,?)', ('Belinda',2))
db.execute('insert into student (name,rank) values (?,?)', ('Jane',3))
db.execute('insert into student (name,rank) values (?,?)', ('Steve',4))
db.execute('insert into student (name,rank) values (?,?)', ('Alfred',5))
db.commit()

# Read Record
records = db.execute('select * from student order by rank desc')
# list(records)
for student in records:
	print(student)

# Update Record
db.execute('update student set rank=? where name=?', (5,'Steve'))
db.execute('update student set rank=? where name=?', (4,'Alfred'))
db.commit()

# Read Record
records = db.execute('select * from student order by rank')

for i in records:
	print(i)

# Delete Record
db.execute('delete from student where rank=5')
db.commit()

# Read Record
def read_records():
    records = db.execute('select * from student order by rank')
    for i in records:
    	print(i)

read_records()

# Challenge
db = sqlite3.connect('school.db')

db.execute('create table subjects (subject text,students int, classes int)')

db.execute('insert into subjects (subject,students, classes) values (?,?,?)',('English',200,10))
db.execute('insert into subjects (subject,students, classes) values (?,?,?)',('Chinese',50,8))
db.execute('insert into subjects (subject,students, classes) values (?,?,?)',('Math',80,12))
db.execute('insert into subjects (subject,students, classes) values (?,?,?)',('Science',80,12))
db.commit()

records = db.execute('select * from subjects order by subject')

for i in records:
	print(i)
