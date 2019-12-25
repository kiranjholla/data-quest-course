import psycopg2 as psg

conn = psg.connect(dbname="postgres", user="postgres", password="my-password")
conn.autocommit = True
cursor = conn.cursor()
cursor.execute("CREATE TABLE notes(id integer PRIMARY KEY, body text, title text)")
conn.close()