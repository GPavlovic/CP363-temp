"""
-------------------------------------------------------
Authors: Braden Poirier, Goran Pavlovic
-------------------------------------------------------
Summary: Client to process inputs from user and call queries.
-------------------------------------------------------
"""
import mysql.connector

db = mysql.connector.connect(user = 'root',
                             host = 'localhost',
                             password = '',
                             database = '')
 
# Present menu to user.

# Switch statement to process input and call specified query.
