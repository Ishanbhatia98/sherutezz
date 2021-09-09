import mysql.connector
try:
    dataBase = mysql.connector.connect(
        host="localhost",
        user="ishan",
        passwd="sherutezz"
    )

# preparing a cursor object
    cursorObject = dataBase.cursor()

# creating database
    cursorObject.execute("CREATE DATABASE records")

    dataBase = mysql.connector.connect(
        host="localhost",
        user="ishan",
        passwd="sherutezz",
        database="records")

# preparing a cursor object
    cursorObject = dataBase.cursor()

# creating table
    deviceRecord = """
CREATE TABLE  devrecords
(
  id              INT unsigned NOT NULL AUTO_INCREMENT, 
  vid             VARCHAR(150) NOT NULL,                
  created           DATETIME NOT NULL,                        
  lat               FLOAT NOT NULL,
  lng               FLOAT NOT NULL,
  c1                FLOAT NOT NULL,
  c2                FLOAT NOT NULL,
  c3                FLOAT NOT NULL,
  c4                FLOAT NOT NULL,
  c5                FLOAT NOT NULL,
  c6                FLOAT NOT NULL,
  c7                FLOAT NOT NULL,
  c8                FLOAT NOT NULL,
  c9                FLOAT NOT NULL,
  c10               FLOAT NOT NULL,
  c11               FLOAT NOT NULL,
  c12               FLOAT NOT NULL,
  c13               FLOAT NOT NULL,
  c14               FLOAT NOT NULL, 
  cav               FLOAT NOT NULL,
  packv             FLOAT NOT NULL,
  curr              FLOAT NOT NULL,
  batp              FLOAT NOT NULL,
  PRIMARY KEY     (id)                                
);
"""


# table created
    cursorObject.execute(deviceRecord)
    dataBase.close()
except Exception as Argument:

    # creating/opening a file
    f = open("errorlogs.txt", "a")

    # writing in the file
    f.write("database - " + str(Argument)+'\n')

    # closing the file
    f.close()
