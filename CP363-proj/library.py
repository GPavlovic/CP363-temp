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
    # Confirm insertion.
    print("{0} was added to the database of actors!".format(name))
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
    # The insert movie SQL statement.
    insert_movie = ("INSERT INTO MOVIE"
                    "(Title, Genre, Rating, Length, ReleaseDate)"
                    "VALUES(%s, %s, %s, %s, %s)")
    # Execute the statement with the given information.
    cursor.execute(insert_movie, movie_info)
    # Make sure the data is committed to the db.
    db.commit();
    # Confirm insertion.
    print("{0} was added to the database of movies!".format(title))
    # Close 
    cursor.close()
    db.close()
    return
"""
-------------------------------------------------------
Query to insert a studio into the database.
-------------------------------------------------------
"""
def insertStudio(db):
    # Get cursor.
    cursor = db.cursor()
    # Get information about the studio from the user.
    name = input("What is the name of the studio?").strip()
    address = input("What is the address of the studio?").strip()
    studio_info = (name, address)
    # The insert studio SQL statement.
    insert_studio = ("INSERT INTO STUDIO"
                    "(Name, Address)"
                    "VALUES(%s, %s)")
    # Execute the statement with the given information.
    cursor.execute(insert_studio, studio_info)
    # Make sure the data is committed to the db.
    db.commit();
    # Confirm insertion.
    print("{0} was added to the database of studios!".format(name))
    # Close 
    cursor.close()
    db.close()
    return

"""
-------------------------------------------------------
Query to insert a channel into the database.
-------------------------------------------------------
"""
def insertChannel(db):
    # Get cursor.
    cursor = db.cursor()
    # Get information about the channel from the user.
    name = input("What is the name of the channel?").strip()
    address = input("What is the address of the channel?").strip()
    channel_info = (name, address)
    # The insert channel SQL statement.
    insert_channel = ("INSERT INTO CHANNEL"
                    "(Name, Address)"
                    "VALUES(%s, %s)")
    # Execute the statement with the given information.
    cursor.execute(insert_channel, channel_info)
    # Make sure the data is committed to the db.
    db.commit();
    # Confirm insertion.
    print("{0} was added to the database of channels!".format(name))
    # Close 
    cursor.close()
    db.close()
    return
"""
-------------------------------------------------------
Query to insert a critic into the database.
-------------------------------------------------------
"""
def insertCritic(db):
    # Get cursor.
    cursor = db.cursor()
    # Get information about the channel from the user.
    name = input("What is the name of the critic?").strip()
    city = input("What city is the critic from?").strip()
    rep = input("What is the reputation of the critic?(x/10)").strip()
    critic_info = (name, city, rep)
    # The insert critic SQL statement.
    insert_critic = ("INSERT INTO CRITIC"
                    "(Name, City, Reputation)"
                    "VALUES(%s, %s, %s)")
    # Execute the statement with the given information.
    cursor.execute(insert_critic, critic_info)
    # Make sure the data is committed to the db.
    db.commit();
    # Confirm insertion.
    print("{0} was added to the database of critics!".format(name))
    # Close 
    cursor.close()
    db.close()
    return
"""
-------------------------------------------------------
Query to remove an actor from the database.
-------------------------------------------------------
"""
def removeActor(db):
    # Get cursor.
    cursor = db.cursor()
    # Get information about the channel from the user.
    name = input("What is the name of the actor?").strip()
    actor_info = (name)
    # The remove actor SQL statement.
    remove_actor = ("DELETE FROM ACTOR"
                    "WHERE Name = %s")
    # Execute the statement with the given information.
    cursor.execute(remove_actor, actor_info)
    # Make sure the data is committed to the db.
    db.commit();
    # Confirm removal.
    print("{0} was removed from the database of actors!".format(name))
    # Close 
    cursor.close()
    db.close()
    return
"""
-------------------------------------------------------
Query to remove an movie from the database.
-------------------------------------------------------
"""
def removeMovie(db):
    # Get cursor.
    cursor = db.cursor()
    # Get information about the channel from the user.
    title = input("What is the name of the movie?").strip()
    movie_info = (title)
    # The remove actor SQL statement.
    remove_movie = ("DELETE FROM MOVIE"
                    "WHERE Title = %s")
    # Execute the statement with the given information.
    cursor.execute(remove_movie, movie_info)
    # Make sure the data is committed to the db.
    db.commit();
    # Confirm removal.
    print("{0} was removed from the database of movies!".format(title))
    # Close 
    cursor.close()
    db.close()
    return

"""
-------------------------------------------------------
Query to remove an studio from the database.
-------------------------------------------------------
"""
def removeStudio(db):
    # Get cursor.
    cursor = db.cursor()
    # Get information about the studio from the user.
    name = input("What is the name of the studio?").strip()
    studio_info = (name)
    # The remove studio SQL statement.
    remove_studio = ("DELETE FROM STUDIO"
                     "WHERE Name = %s")
    # Execute the statement with the given information.
    cursor.execute(remove_studio, studio_info)
    # Make sure the data is committed to the db.
    db.commit();
    # Confirm removal.
    print("{0} was removed from the database of studios!".format(name))
    # Close 
    cursor.close()
    db.close()
    return

"""
-------------------------------------------------------
Query to remove an critic from the database.
-------------------------------------------------------
"""
def removeCritic(db):
    # Get cursor.
    cursor = db.cursor()
    # Get information about the critic from the user.
    name = input("What is the name of the critic?").strip()
    critic_info = (name)
    # The remove critic SQL statement.
    remove_critic = ("DELETE FROM CRITIC"
                     "WHERE Name = %s")
    # Execute the statement with the given information.
    cursor.execute(remove_critic, critic_info)
    # Make sure the data is committed to the db.
    db.commit();
    # Confirm removal.
    print("{0} was removed from the database of critics!".format(name))
    # Close 
    cursor.close()
    db.close()
    return


"""
-------------------------------------------------------
Query to remove an movie from the database.
-------------------------------------------------------
"""

def removeChannel(db):
    # Get cursor.
    cursor = db.cursor()
    # Get information about the channel from the user.
    name = input("What is the name of the channel?").strip()
    channel_info = (name)
    # The remove actor SQL statement.
    remove_channel = ("DELETE FROM CHANNEL"
                      "WHERE Name = %s")
    # Execute the statement with the given information.
    cursor.execute(remove_channel, channel_info)
    # Make sure the data is committed to the db.
    db.commit();
    # Confirm removal.
    print("{0} was removed from the database of channels!".format(name))
    # Close 
    cursor.close()
    db.close()
    return

"""
-------------------------------------------------------
Query to read actor from the database.
-------------------------------------------------------
"""

def readActor(db):
    # Get cursor.
    cursor = db.cursor()
    # Get information about the actor from the user.
    name = input("What is the name of the actor?").strip()
    actor_info = (name)
    # The read actor SQL statement.
    read_actor = ("SELECT Name, City" 
                    "FROM ACTOR"
                    "WHERE Name = %s")
    # Execute the statement with the given information.
    cursor.execute(read_actor, actor_info)
    # Make sure the data is committed to the db.
    db.commit();
    # Confirm.
    print("Found! Actor: {0} City: {1}".format(cursor.Name, cursor.City))
    # Close 
    cursor.close()
    db.close()
    return

"""
-------------------------------------------------------
Query to read movie from the database.
-------------------------------------------------------
"""

def readMovie(db):
    # Get cursor.
    cursor = db.cursor()
    # Get information about the movie from the user.
    title = input("What is the title of the movie?").strip()
    movie_info = (title)
    # The read movie SQL statement.
    read_movie = ("SELECT Title, Genre, Rating, Length, ReleaseDate" 
                    "FROM MOVIE"
                    "WHERE Title = %s")
    # Execute the statement with the given information.
    cursor.execute(read_movie, movie_info)
    # Make sure the data is committed to the db.
    db.commit();
    # Confirm.
    print("Found! Movie: {0} Genre: {1} Rating: {2} Length: {3} Release Date: {4}".format(cursor.Title, cursor.Genre, cursor.Rating, cursor.Length, cursor.ReleaseDate))
    # Close 
    cursor.close()
    db.close()
    return

"""
-------------------------------------------------------
Query to read studio from the database.
-------------------------------------------------------
"""

def readStudio(db):
    # Get cursor.
    cursor = db.cursor()
    # Get information about the studio from the user.
    name = input("What is the name of the studio?").strip()
    studio_info = (name)
    # The read studio SQL statement.
    read_studio = ("SELECT Name, Address" 
                    "FROM STUDIO"
                    "WHERE Name = %s")
    # Execute the statement with the given information.
    cursor.execute(read_studio, studio_info)
    # Make sure the data is committed to the db.
    db.commit();
    # Confirm.
    print("Found! Studio: {0} Address: {1}".format(cursor.Name, cursor.Address))
    # Close 
    cursor.close()
    db.close()
    return

"""
-------------------------------------------------------
Query to read channel from the database.
-------------------------------------------------------
"""

def readChannel(db):
    # Get cursor.
    cursor = db.cursor()
    # Get information about the channel from the user.
    name = input("What is the name of the channel?").strip()
    channel_info = (name)
    # The read channel SQL statement.
    read_channel = ("SELECT Name, Address" 
                    "FROM CHANNEL"
                    "WHERE Name = %s")
    # Execute the statement with the given information.
    cursor.execute(read_channel, channel_info)
    # Make sure the data is committed to the db.
    db.commit();
    # Confirm.
    print("Found! Channel: {0} Address: {1}".format(cursor.Name, cursor.Address))
    # Close 
    cursor.close()
    db.close()
    return

"""
-------------------------------------------------------
Query to read critic from the database.
-------------------------------------------------------
"""

def readCritic(db):
    # Get cursor.
    cursor = db.cursor()
    # Get information about the critic from the user.
    name = input("What is the name of the critic?").strip()
    critic_info = (name)
    # The read critic SQL statement.
    read_critic = ("SELECT Name, Address, Reputation" 
                    "FROM CRITIC"
                    "WHERE Name = %s")
    # Execute the statement with the given information.
    cursor.execute(read_critic, critic_info)
    # Make sure the data is committed to the db.
    db.commit();
    # Confirm.
    print("Found! Critic: {0} Address: {1} Reputation: {2}".format(cursor.Name, cursor.Address, cursor.Reputation))
    # Close 
    cursor.close()
    db.close()
    return