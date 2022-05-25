import sqlite3

con = sqlite3.connect('items.db')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS food_solid
                    (item text PRIMARY KEY, serving real, calories real, protein real, carbs real, fat real)''')
cur.execute('''CREATE TABLE IF NOT EXISTS food_liquid
                    (item text PRIMARY KEY, serving real, calories real, protein real, carbs real, fat real)''')
cur.execute('''CREATE TABLE IF NOT EXISTS drink
                    (item text PRIMARY KEY, serving real, calories real, protein real, carbs real, fat real)''')

con.commit()
