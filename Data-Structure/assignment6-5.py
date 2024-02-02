
text = "X-DSPAM-Confidence:    0.8475"
number = text.find('0')
print(float(text[number:])) # by not giving the second argument, it will start from the first occurence of the given string and go till the end