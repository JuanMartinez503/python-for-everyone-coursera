
def computepay (h , r):
    if h>40:
        pay = 40*r + (h-40)*1.5*r
    else:
        pay = h*r
    return pay

hrs = input("Enter Hours:")     
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
p = computepay(h,r)    
print("Pay", p)