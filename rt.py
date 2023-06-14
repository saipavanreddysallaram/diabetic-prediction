import sqlite3

conn=sqlite3.connect('patient.db')

cur=conn.cursor()
#cur.execute("create table patient_details('patient name' varchar(30),'result' varchar(30))")
cur.execute("insert into patient_details values('sanjay','non diabetic')")
conn.commit()