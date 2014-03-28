"""
-------------------------------------------------------
Authors: Braden Poirier, Goran Pavlovic
-------------------------------------------------------
Summary: Collection of queries for the database.
-------------------------------------------------------
"""
import mysql.connector

"""
-------------------------------------------------------
Query to insert an actor into the database.
-------------------------------------------------------
"""
def insertActor(db):
    # Get cursor.
    cursor = db.cursor()
    # Get information about the actor from the user.
    name = input("What is the name of the actor?").strip()
    city = input("What city is the actor from?").strip()
    actor_info = (name, city)
    # The insert actor SQL statement.
    insert_actor = ("INSERT INTO ACTOR "
                    "(Name, City) "
                    "VALUES(%s, %s)")
    # Execute the statement with the given information.
    cursor.execute(insert_actor, actor_info)
    # Make sure the data is committed to the db.
    db.commit();
    # Close 
    cursor.close()
    db.close()
    return

"""
-------------------------------------------------------
Query to insert a movie into the database.
-------------------------------------------------------
"""
def insertMovie(db):
    # Get cursor.
    cursor = db.cursor()
    # Get information about the movie from the user.
    title = input("What is the title of the movie?").strip()
    genre = input("What is the genre of the movie?").strip()
    rating = input("What is the rating of the movie?").strip()
    length = input("What is the length of the movie?").strip()
    release = input("What is the release date of the movie?(dd/mm/yyyy)").strip()
    movie_info = (title, genre, rating, length, release)
    # The insert actor SQL statement.
    insert_movie = ("INSERT INTO MOVIE"
                    "(Title, Genre, Rating, Length, ReleaseDate)"
                    "VALUES(%s, %s, %s, %s, %s)")
    # Execute the statement with the given information.
    cursor.execute(insert_movie, movie_info)
    # Make sure the data is committed to the db.
    db.commit();
    # Close 
    cursor.close()
    db.close()
    return