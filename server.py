import socket
import pickle
import time
import mysql.connector
try:
    dataBase = mysql.connector.connect(
        host="localhost",
        user="ishan",
        passwd="sherutezz",
        database='records',
        autocommit=True

    )
# preparing a cursor object
    cursor = dataBase.cursor()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 1234))
# port number can be anything between 0-65535(we usually specify non-previleged ports which are > 1023)
    s.listen(5)

    while True:
        clt, adr = s.accept()
        print(f"Connection to {adr}established")
   # f string is literal string prefixed with f which
   # contains python expressions inside braces
        clt.send(bytes("Connection established!", "utf-8 "))

        data = b""
        while True:
            packet = clt.recv(4096)
            if not packet:
                break
            data += packet

        data = pickle.loads(data)

        time.sleep(20)

        for row in data:
            tdata = row['tdata'].split(',')
            c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14 = tdata[3], tdata[4], tdata[5], tdata[6], tdata[
                7], tdata[8], tdata[9], tdata[10], tdata[11], tdata[12], tdata[13], tdata[14], tdata[15], tdata[15]
            query = """INSERT INTO `devrecords` (vid, created, lat, lng, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, cav, packv, curr, batp) 
        VALUES (%(vid)s, %(created)s, %(lat)s, %(lng)s, %(c1)s, %(c2)s,  %(c3)s, %(c4)s, %(c5)s, %(c6)s, %(c7)s, %(c8)s, %(c9)s, %(c10)s, %(c11)s, %(c12)s, %(c13)s, %(c14)s, %(cav)s, %(pv)s,%(curr)s, %(batp)s);"""

            d_vals = {
                'vid': row['vid'],
                'created': row['created'],
                'lat': tdata[1],
                'lng': tdata[2],
                'c1': c1,
                'c2': c2,
                'c3': c3,
                'c4': c4,
                'c5': c5,
                'c6': c6,
                'c7': c7,
                'c8': c8,
                'c9': c9,
                'c10': c10,
                'c11': c11,
                'c12': c12,
                'c13': c13,
                'c14': c14,
                'cav': tdata[18],
                'pv': tdata[19],
                'curr': tdata[20],
                'batp': tdata[21]

            }
            cursor.execute(query, d_vals)

    s.close()
    dataBase.close()

except Exception as Argument:

    # creating/opening a file
    f = open("errorlogs.txt", "a")

    # writing in the file
    f.write('server - ' + str(Argument)+'\n')

    # closing the file
    f.close()
