#!/usr/bin/env python

import argparse
import sqlite3
import datetime

conn = sqlite3.connect('/home/wasp/utils/expenses.db')
c = conn.cursor()
parser = argparse.ArgumentParser(description='Personal expenses manager.')

parser.add_argument("-a", "--add", dest="add", default="", help="Adds a voice to the database.", metavar="DESCRIPTION")

parser.add_argument("-p", "--price", dest="price", default="", help="Specifies the amount of the expense.", metavar="PRICE")

parser.add_argument("-d", "--date", dest="date", default="", help="Specifies the date of the expense. Optional.", metavar="YYYY-MM-DD")

parser.add_argument("-l", "--list", dest="lst", action="store_true", default="False", help="Lists expenses in the database.")

parser.add_argument("-o", "--order", dest="orderby", action="store", default="date", help="Orders the list according to one field of the table. Possible values: date, price, desc. The default is date.", metavar="date")

parser.add_argument("-t", "--type", dest="ordertype", default="asc", help="Specifies if the order is ascendent (asc) or descendent (desc). The default is asc.", metavar="asc")

options = parser.parse_args()

if options.add != "":
  c.execute('''insert into expenses(date, desc, price) values (?, ?, ?)''', (datetime.date.today() if options.date == "" else options.date, options.add, float(options.price)))
  conn.commit()

if options.lst == True:
  c.execute("select * from expenses order by " + options.orderby + " " + options.ordertype)
  rows = c.fetchall()
  for row in rows:
    print('On ' + str(row[0]) + ' you bought ' + str(row[1]) + ' for ' + str(row[2]) +'.')
