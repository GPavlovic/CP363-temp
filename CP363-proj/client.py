import library
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
print( "Please select one of the following operations (1-4): " )
print( "1 - Insert" )
print( "2 - Retrieve" )
print( "3 - Remove" )
print( "4 - Exit" )

opChoice=int(input())
if(opChoice==1):
    print( "Please select one of the following attributes (1-6): " )
    print( "1 - Insert Actor" )
    print( "2 - Insert Movie" )
    print( "3 - Insert Studio" )
    print( "4 - Insert Channel" )
    print( "5 - Insert Critic" )
    print( "6 - Exit" )
    attChoice=int(input())
    if(attChoice==1):
        library.insertActor(db)
    elif(attChoice==2):
        library.insertMovie(db)
    elif(attChoice==3):
        library.insertStudio(db)
    elif(attChoice==4):
        library.insertChannel(db)
    elif(attChoice==5):
        library.insertCritic(db)
    elif(attChoice==6):
        return
    else:
        print( "Error. Incorrect Input." )
elif(opChoice==2):
    print( "Please select one of the following attributes (1-6): " )
    print( "1 - Retrieve Actor" )
    print( "2 - Retrieve Movie" )
    print( "3 - Retrieve Studio" )
    print( "4 - Retrieve Channel" )
    print( "5 - Retrieve Critic" )
    print( "6 - Exit" )
    attChoice=int(input())
    if(attChoice==1):
        library.readActor(db)
    elif(attChoice==2):
        library.readMovie(db)
    elif(attChoice==3):
        library.readStudio(db)
    elif(attChoice==4):
        library.readChannel(db)
    elif(attChoice==5):
        library.readCritic(db)
    elif(attChoice==6):
        return
    else:
        print( "Error. Incorrect Input." )
elif(opChoice==3):
    print( "Please select one of the following attributes (1-6): " )
    print( "1 - Remove Actor" )
    print( "2 - Remove Movie" )
    print( "3 - Remove Studio" )
    print( "4 - Remove Channel" )
    print( "5 - Remove Critic" )
    print( "6 - Exit" )
    attChoice=int(input())
    if(attChoice==1):
        library.removeActor(db)
    elif(attChoice==2):
        library.removeMovie(db)
    elif(attChoice==3):
        library.removeStudio(db)
    elif(attChoice==4):
        library.removeChannel(db)
    elif(attChoice==5):
        library.removeCritic(db)
    elif(attChoice==6):
        return
    else:
        print( "Error. Incorrect Input." )
elif(opChoice==4):
    return
else:
    print( "Error. Incorrect Input." )

