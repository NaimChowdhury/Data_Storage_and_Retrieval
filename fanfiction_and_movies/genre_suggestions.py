import sys
import psycopg2


print("Welcome to Jeeda and Naeem's film search program! Connecting to the film database.")
# Connects to the movies database on the NCF server.
conn= psycopg2.connect("dbname=movies user=nchowdhury")
time.sleep(3)
response= input ("Please enter the name of a film (case sensitive): ")
while response== '':
        response= input ("No input detected (case sensitive): ")