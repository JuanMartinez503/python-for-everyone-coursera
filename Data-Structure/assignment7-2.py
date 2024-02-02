
fh = input("Enter file name: ")
try:
    count = 0
    total = 0
    
    fhand = open(fh)
    for line in fhand:
        if line.startswith('X-DSPAM-Confidence:'):
            number = line.find('0')
            other = float(line[number:])
            count = count + 1
            total = total + other
    print('Average spam confidence:', total/count)
except:
    print('File cannot be opened:', fh)
    quit()