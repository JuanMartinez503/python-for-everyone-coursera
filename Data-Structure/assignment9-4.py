fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
d = dict()
for line in fh:
    line = line.rstrip()
    if line.startswith("From "):
        words = line.split()
        d[words[1]] = d.get(words[1], 0) + 1
big_count = None
big_word = None
for word, count in d.items():
    if big_count is None or count > big_count:
        big_word = word
        big_count = count
print(big_word, big_count)
