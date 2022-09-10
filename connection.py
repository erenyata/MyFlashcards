import mysql.connector
conncection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "****", #use your own 
        database = "flashcards"
    )