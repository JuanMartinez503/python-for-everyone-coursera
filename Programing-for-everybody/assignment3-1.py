
# in python space does matter
# try and except are reserved words in python, try is there to try the code and except is there to catch the exception so the code does not crash

hrs = input("Enter Hours:")
h=float(hrs)
rate = input("Enter Rate:")
r=float(rate)
pay = h*r
if h>40:
    pay = 40*r + (h-40)*1.5*r   # if the hours are more than 40 then the pay will be 40 hours at the rate and the rest of the hours at 1.5 times the rate
print("Pay:", pay)