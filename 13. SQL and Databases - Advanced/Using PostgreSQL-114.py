## 3. Psycopg2 ##

import psycopg2 as psg
conn = psg.connect("dbname=dq user=dq")
cur = conn.cursor()
print(cur)
conn.close()

## 4. Creating a table ##

import psycopg2 as psg

create_query = (
    'CREATE TABLE notes('
    '   id INTEGER,'
    '   body TEXT,'
    '   title TEXT'
    ')'
)

conn = psg.connect("dbname=dq user=dq")
cur = conn.cursor()

cur.execute(create_query)

conn.close()

## 5. SQL Transactions ##

import psycopg2 as psg

drop_query = 'DROP TABLE notes';
create_query = (
    'CREATE TABLE notes('
    '   id INTEGER,'
    '   body TEXT,'
    '   title TEXT'
    ')'
)

conn = psg.connect("dbname=dq user=dq")
cur = conn.cursor()

cur.execute(drop_query)
conn.commit()

cur.execute(create_query)

conn.commit()
conn.close()

## 6. Autocommitting ##

import psycopg2 as psg

drop_query = ('DROP TABLE facts')
create_query = (
    'CREATE TABLE facts('
    '   id INTEGER,'
    '   country TEXT,'
    '   value TEXT'
    ')'
)

conn = psg.connect("dbname=dq user=dq")
conn.autocommit = True

cur = conn.cursor()

cur.execute(drop_query)
cur.execute(create_query)

conn.close()

## 7. Executing queries ##

import psycopg2 as psg

drop_query = ('DROP TABLE facts')
create_query = (
    'CREATE TABLE facts('
    '   id INTEGER,'
    '   country TEXT,'
    '   value TEXT'
    ')'
)
insert_query = "INSERT INTO notes VALUES (1, 'Do more missions on Dataquest.', 'Dataquest reminder')"

select_query = 'SELECT * FROM notes'

conn = psg.connect("dbname=dq user=dq")
conn.autocommit = True

cur = conn.cursor()

cur.execute(insert_query)
cur.execute(select_query)
result = cur.fetchall()

print(result)
conn.close()

## 8. Creating a database ##

import psycopg2 as psg

drop_query = "DROP DATABASE IF EXISTS income"
create_query = "CREATE DATABASE income OWNER dq"

insert_query = "INSERT INTO notes VALUES (1, 'Do more missions on Dataquest.', 'Dataquest reminder')"

select_query = 'SELECT * FROM notes'

conn = psg.connect("dbname=dq user=dq")
conn.autocommit = True

cur = conn.cursor()

cur.execute(drop_query)
cur.execute(create_query)

conn.close()

## 9. Deleting a database ##

import psycopg2 as psg

drop_query = "DROP DATABASE IF EXISTS income"
create_query = "CREATE DATABASE income OWNER dq"

insert_query = "INSERT INTO notes VALUES (1, 'Do more missions on Dataquest.', 'Dataquest reminder')"

select_query = 'SELECT * FROM notes'

conn = psg.connect("dbname=dq user=dq")
conn.autocommit = True

cur = conn.cursor()

cur.execute(drop_query)

conn.close()