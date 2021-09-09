import socket
import pickle
import time
import json
import mysql.connector
from urllib.request import urlopen


def last_inserted_timestamp(n, last):
    for i in range(n-1, -1, -1):
        if data[i]['created'] == last:
            return i
    return -1


try:
    # cronjob

    dataBase = mysql.connector.connect(
        host="localhost",
        user="ishan",
        passwd="sherutezz",
        database='records',
        autocommit=True

    )
# preparing a cursor object
    cursor = dataBase.cursor()

    query = 'select * from devrecords ORDER BY id DESC LIMIT 1;'
    cursor.execute(query)
    last_timestamp = cursor.fetchall()
    last_timestamp = last_timestamp[0][2]

    url = 'http://13.233.13.254:2222/xenergyData.json'
    response = urlopen(url)
    data = json.loads(response.read())
    data = data['records']
    n = len(data)
    current_timestamp = data[n-1]['created']

    if last_timestamp != current_timestamp:
        # last_inserted_timestamp
        lits = last_inserted_timestamp(n,  last_timestamp)
        if lits != -1:
            for i in range(lits+1, n):
                tdata = data[i]['tdata'].split(',')
            c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14 = tdata[3], tdata[4], tdata[5], tdata[6], tdata[
                7], tdata[8], tdata[9], tdata[10], tdata[11], tdata[12], tdata[13], tdata[14], tdata[15], tdata[15]
            query = """INSERT INTO `devrecords` (vid, created, lat, lng, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, cav, packv, curr, batp) 
        VALUES (%(vid)s, %(created)s, %(lat)s, %(lng)s, %(c1)s, %(c2)s,  %(c3)s, %(c4)s, %(c5)s, %(c6)s, %(c7)s, %(c8)s, %(c9)s, %(c10)s, %(c11)s, %(c12)s, %(c13)s, %(c14)s, %(cav)s, %(pv)s,%(curr)s, %(batp)s);"""

            d_vals = {
                'vid': data[i]['vid'],
                'created': data[i]['created'],
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
        else:
            f = open("errorlogs.txt", "a")

            # writing in the file
            f.write(f'update - {last_timestamp}  not present in dataset\n')

            # closing the file
            f.close()
        print('Database updated!')
    else:
        print('Database is upto date!')

except Exception as Argument:

    # creating/opening a file
    f = open("errorlogs.txt", "a")

    # writing in the file
    f.write('update - ' + str(Argument)+'\n')

    # closing the file
    f.close()
