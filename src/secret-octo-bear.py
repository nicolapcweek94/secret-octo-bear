#!/usr/bin/env python

import argparse
import sqlite3
import datetime

conn = sqlite3.connect('expenses.db')
c = conn.cursor()
parser = argparse.ArgumentParser(description='Personal expenses manager.')

parser.add_argument("-a", "--add", dest="add", default="", help="Adds a voice to the database.", metavar="DESCRIPTION")

parser.add_argument("-p", "--price", dest="price", default="", help="Specifies the amount of the expense.", metavar="PRICE")

parser.add_argument("-d", "--date", dest="date", default="", help="Specifies the date of the expense. Optional.", metavar="YYYY-MM-DD")

parser.add_argument("-l", "--list", dest="list", action="store_true", default="False", help="Lists expenses in the database.")

options = parser.parse_args()

if options.add != "":
  c.execute('''insert into expenses(date, desc, price) values (?, ?, ?)''', (datetime.date.today() if options.date == "" else options.date, options.add, float(options.price)))
  conn.commit()

if options.list == True:
  c.execute('''select * from expenses order by date''')
  rows = c.fetchall()
  for row in rows:
    print(row)
