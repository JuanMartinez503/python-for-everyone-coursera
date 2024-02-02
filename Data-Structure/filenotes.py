fhand= open('file name')
count = 0 
for line in fhand:
    count = count + 1
    # it can count the number of lines in the file  
    
otherfile = open('file name')
inp = otherfile.read()
print(len(inp)) # it will print the length of the file by characters and not by lines

for line in otherfile:
    line = line.rstrip() # it will remove the white spaces from the right side of the string
    if not line.startswith('From:'):
        continue    # it will skip the lines that start with 'From:'
    if line.startswith('From:'):
        print(line) # it will print the lines that start with 'From:'