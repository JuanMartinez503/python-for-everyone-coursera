import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

url = input('Enter URL: ')
position = int(input('Enter position: ')) - 1  # Adjust for zero-based indexing
count = int(input('Enter count: '))
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

for _ in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    tag = tags[position]

    # Extract the href attribute value
    url = tag.get('href', None)
    print("Retrieving:", url)

print("Last name in sequence:", tag.contents[0])
