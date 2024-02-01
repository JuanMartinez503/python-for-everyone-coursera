
score = input("Enter Score: ")  
try:
    s = float(score)
    if s>=0.9:
        print("A")
    elif s>=0.8:
        print("B")
    elif s>=0.7:
        print("C")
    elif s>=0.6:
        print("D")
    elif s<0.6:
        print("F")
except ValueError:
    print("Error, please enter a number between 0.0 and 1.0.")
    quit()