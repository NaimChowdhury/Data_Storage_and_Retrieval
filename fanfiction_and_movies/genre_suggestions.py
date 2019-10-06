import sys
import psycopg2
import time


print("Welcome to Jeeda and Naeem's film search program! Connecting to the film database.")
# Connects to the movies database on the NCF server.
conn= psycopg2.connect("dbname=movies user=nchowdhury")
time.sleep(3)
response= input ("Please enter the name of a film (case sensitive): ")
while query== '':
        query= input ("No input detected. Please remember how to type, and enter the name of a film (case sensitive): ")

# Initiates the cursor object in psql
cur= conn.cursor()
cur.execute("SELECT genre FROM movies WHERE title='"+query+"';")
# Captures the results of the query in an array of tuples.
results = cur.fetchall()
#print(results)

while results == []:
    cur.execute("SELECT title FROM movies WHERE LOWER(title) like LOWER('"+query+"');")
    results = cur.fetchall()
    # stores the first entry of each tuple in results as in a list
    resembling = [toople[0] for toople in results]
    print("We're sorry, we could not find a film of that name. Did you mean any of the following?")
    # for loop prints films that resemble the input query
    for i in resembling:
        print(i)
    query2 = ("Please type the name of the film, or 'no'. ")
