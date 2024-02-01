# slicing strings 
s = 'Monty Python'      
print(s[0:4]) # Mont
# stops at 4th index
# you can use the in operator to see if one string is in another string
# find() method finds the occurence and returns the index of the first occurence
greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane') # Hello Jane'
example = '      hello world     '
print(example.strip()) # hello world , removes the white spaces from the beginning and end  of the string
line = 'Please have a nice day'
print(line.startswith('Please')) # True, checks if the string starts with the given string
print(line.startswith('p')) # False
# you can give the find method something and a second argument to tell it where to start looking