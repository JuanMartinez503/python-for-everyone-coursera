import urllib.request, urllib.parse, urllib.error
counts = dict()
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip()) # decode() returns a string, strip() removes the leading and trailing whitespaces
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        
print(counts)
    