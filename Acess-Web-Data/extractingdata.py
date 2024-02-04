import re

data = open('data.txt')
regex = '[0-9]+'
numbers = list()
for line in data:
    numbers += re.findall(regex, line)
numbers = [int(i) for i in numbers] # Convert string to int 
print(sum(numbers))
