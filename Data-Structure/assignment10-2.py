fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
d = dict()
for line in fh:
    line = line.rstrip()
    if line.startswith("From "):
        words = line.split()
        long_hour = words[5]
        hour = long_hour[:2]
        d[hour] = d.get(hour, 0) + 1

for k, v in sorted(d.items()):
    print(k, v)