import sys
import psycopg2


print("Welcome to Jeeda and Naeem's film search program! Connecting to the film database.")
# Connects to the movies database on the NCF server.
conn= psycopg2.connect("dbname=movies user=nchowdhury")
time.sleep(3)
response= input ("Please enter the name of a film (case sensitive): ")
while query== '':
        query= input ("No input detected. Please remember how to type, and enter the name of a film (case sensitive): ")

# Initiates the cursor object in psql
cur= conn.cursor()
cur.execute("select genre from movies where title='"+query+"';")
# Captures the results of the query in an array of tuples.
results = cur.fetchall()
#print(results)