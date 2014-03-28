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
Query to insert an actor to the database.
-------------------------------------------------------
"""
def insertActor(db):
    cursor = db.cursor()
    statement = 'SELECT * FROM Employee'
    cursor.execute(statement)
    rows = cursor.fetchall()

    # Make sure the data is committed to the db
    db.commit();

    cursor.close()
    db.close()