import sqlite3 as sql

con = sql.connect("data.db")
cur = con.cursor()
statement = "SELECT username, password FROM std "
cur.execute(statement)
print(cur.fetchall())




# from werkzeug.security import generate_password_hash
# import sqlite3 as sql
#
# # Database connection
# con = sql.connect("data.db")
# cur = con.cursor()
#
# # Create the `std` table if it doesn't exist
# cur.execute('''CREATE TABLE IF NOT EXISTS std
#                (id INTEGER PRIMARY KEY, username TEXT NOT NULL, password TEXT NOT NULL)''')
#
# # Hostel warden details
# username = '2021bcs0093'
# password = 'Karthik'
# hashed_password = generate_password_hash(password)
#
# # Insert the hostel warden into the database
# cur.execute("INSERT INTO std (username, password) VALUES (?, ?)", (username, hashed_password))
#
# # Commit and close the connection
# con.commit()
# con.close()

