import psycopg2
import time

# Establish connection to database
conn= psycopg2.connect("dbname=fanfiction user=nchowdhury")

print("Welcome to JnN Fanfiction Wonderland. What sort of trash are you into? Please do not include apostrophes, articles, or conjuctions.")
query = input("I'm looking for fanfiction related to: ")
print("Thank you. One moment while we scour our databases for things related to %s.", query)

# In order to prepare the string for regular expressions, a for loop will prepare the expression
query = query.split()
string = '('
for i in range(len(query)):
    if i == len(query)-1:
        string += query[i] + ')'
    else:
        string += query[i] + '|'

query = string
print(query)

cur = conn.cursor()

cur.execute("SELECT title, description FROM stories WHERE title ~* '"+query+"' ORDER
BY random() LIMIT 10;")
results = cur.fetchall()
print(results)

