import sys
import psycopg2
import time


print("Welcome to Jeeda and Naeem's film search program! Connecting to the film database.")
# Connects to the movies database on the NCF server.
conn= psycopg2.connect("dbname=movies user=nchowdhury")
time.sleep(1.5)
query = input ("Please enter the name of a film (case sensitive): ")
query2 = query
while query == '':
        query= input ("No input detected. Please remember how to type, and enter the name of a film (case sensitive): ")

# Initiates the cursor object in psql
cur= conn.cursor()
cur.execute("SELECT genre FROM movies WHERE title='"+query+"';")
# Captures the results of the query in an array of tuples.
results = cur.fetchall()
#print(results)

while results == []:
    cur.execute("SELECT title FROM movies where (SELECT show_trgm('"+query+"')) && (SELECT show_trgm(title)) ORDER BY levenshtein('"+query+"',title) limit 5;")
    # cur.execute("SELECT title FROM movies WHERE LOWER(title) like LOWER('"+query+"');")
    results = cur.fetchall()
    # stores the first entry of each tuple in results as in a list
    resembling = [toople[0] for toople in results]
    print("We're sorry, we could not find a film of that name. Did you mean any of the following?")
    # for loop prints films that resemble the input query
    for i in resembling:
        print(i)
    query2 = input("Please type the name of the film, or 'no'. ")

# instantiates a distance counter that will iterate each time "no" is entered
lev_dist = 3

# If the first query does not find their movie, this while loop will search using an increasing levenshtein distance
while query2 == 'no' and lev_dist < 7:
    lev_dist += + 1
    cur.execute("SELECT title, levenshtein FROM (SELECT title, levenshtein(title, '"+query+"') levenshtein FROM movies) levenbois WHERE levenshtein < "+str(lev_dist)+" ;")
    results2 = cur.fetchall()
    resembling2 = [toople[0] for toople in results2]
    print("Hmmm. How about any of these? It had better be in this list. ")
    time.sleep(1)
    for i in resembling2:
        print(i)
    query2 = input("Please type the name of the film, or 'no'. ")

# Now that the movie has likely been found, the program searches for the genre cube datatype
if query2 is not 'no' or query2 is not '' or results is not []:
    cur.execute("SELECT genre FROM movies WHERE title = '"+query2+"';")
    genre = cur.fetchall()
    if genre == []:
        print("We're sorry. We could not find a genre for that title. Restart our glorious application and try again.")
    else:
        genre_cube = genre[0][0]  #scoop up the genre cube from the tuple in list
        cur.execute("SELECT title, genre FROM movies WHERE cube_distance(genre,'"+genre_cube+"') < 7;")
        titletoops= cur.fetchall()
        titles = [toople[0] for toople in titletoops]
        print("Here are some films we thought you would like, based on the genre of the title you chose! Enjoy! ", titles)
        for title in titles:
            print (title)
            time.sleep(.5)
        print("All done. Enjoy your films!")