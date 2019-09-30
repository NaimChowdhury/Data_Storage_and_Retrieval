import string
import matplotlib.pyplot as pl
import numpy as np


#psycopg2 is a package that allows python to communicate with psql
import psycopg2

# initiates the connection with the database
conn = psycopg2.connect("dbname=movies user=nchowdhury")
cur = conn.cursor()

# executes the following query in psql
cur.execute("select title from movies limit 10;")
# titles stores the result of the query as an array filled with tuples
titles = cur.fetchall()

# each film in titles is a 2-tuple with an empty second element
for film in titles:
    print(film[0])
