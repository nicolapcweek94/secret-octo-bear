import sqlite3

conn = sqlite3.connect('expenses.db')
c = conn.cursor()

c.execute('''create table expenses (date date, desc text, price real)''') #Creates the table we use to store data

conn.commit() #Commits the changes to the DB

c.close()
