import mysql.connector

db = mysql.connector.connect(user = 'root',
                             host = 'localhost',
                             password = '',
                             database = '')

cursor = db.cursor()
statement = 'SELECT * FROM Employee'
cursor.execute(statement)
rows = cursor.fetchall()

# Make sure the data is committed to the db
db.commit();

cursor.close()
db.close()