import json
import socket
from urllib.request import urlopen
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))


msg = s.recv(1024)
print(msg.decode("utf-8"))


url = 'http://13.233.13.254:2222/xenergyData.json'
response = urlopen(url)
data = json.loads(response.read())
data = pickle.dumps(data['records'])
s.send(data)
s.close()
