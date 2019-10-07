import psycopg2
import time

conn= psycopg2.connect("dbname=fanfiction user=nchowdhury")

print("Welcome to JnN Fanfiction Wonderland. What sort of trash are you into?")
query = input("I'm looking for fanfiction related to: ")
print("Thank you. One moment while we scour our databases for things related to %s.", query)

cur = conn.cursor()

