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

# 'histogram is a dictionary that will have a key for each potenial'
# 'number of words in a film title' 
histogram = {}

# each film in titles is a 2-tuple with an empty second element
for film in titles:
    # print(film[0])
    # stores the name of each film as an array with an element for each word
    film_str = str.split(film[0])
    # stores the number of words in the title
    name_len = len(film_str)

    # if the dictionary key doesn't already exist, make it.
    if name_len not in histogram:
        histogram.update( {name_len : 1} )
    else:
        histogram[name_len] = histogram[name_len] +1

print("The number of occurrences for each title length is: ", histogram)

def asterisk_plot(dictionary):
    for i in dictionary.keys():
        output = ''
        times = dictionary[i]
        while( times > 0):
            output += '*'
            times = times -1
        print(dictionary[i], " : ", output)

asterisk_plot(histogram)

