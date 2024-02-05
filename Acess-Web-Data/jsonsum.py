import urllib.request, urllib.parse, urllib.error
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()   # read() returns a bytes object, decode() returns a string  
print('Retrieved', len(data), 'characters')
info = json.loads(data)
print('Count:', len(info['comments']))
sum = 0
for item in info['comments']:
    sum = sum + int(item['count'])
print('Sum:', sum)