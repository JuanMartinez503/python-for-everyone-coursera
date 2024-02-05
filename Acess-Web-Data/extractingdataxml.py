import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data_url = 'https://py4e-data.dr-chuck.net/comments_1973981.xml'
data = urllib.request.urlopen(data_url, context=ctx).read()
tree = ET.fromstring(data)
counts = tree.findall('.//count')
sum = 0
for count in counts:
    sum = sum + int(count.text)
print(sum)