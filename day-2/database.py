import mysql.connector
con = mysql.connector.connect(host='localhost', user='root', password='', database='python')
try:
    print(con.connection_id)
except:
    print("connection fail")
    
curo = con.cursor()
#create database
#q1 = "create database python"
#curo.execute(q1)

#create table
#q2 = 'create table student(id integer(4), name varchar(20) , cgpa float)'
#curo.execute(q2)

q3 = 'insert into student values(%s , %s , %s)'
r1 = (1,'prachi',9.1)
r2 = (2,'ayushi',8.1)
r3 = (3,'dhruvi',9.0)

curo.execute(q3,r1)
curo.execute(q3,r2)
curo.execute(q3,r3)
print('Inserted data')
#read table
print('Read data')
q4 = 'select * from student'
curo.execute(q4)
r= curo.fetchall()
for val in r:
    print(val)

# update table

q5 = 'update student set cgpa=9.0 where name="ayushi"'
curo.execute(q5)
print('Updated data')
q6 = 'select * from student'
curo.execute(q6)
r= curo.fetchall()
for val in r:
    print(val)

# delete table

q7 = 'delete from student where name="dhruvi"'
curo.execute(q7)
print('data after delete name=dhruvi')
q8 = 'select * from student'
curo.execute(q8)
r= curo.fetchall()
for val in r:
    print(val)
