# classes are a way to group data and functions together. The data is referred to as attributes and the functions are referred to as methods.

# The simplest class possible is shown below:
class PartyAnimal:
    
    x = 0
    def __init__(self) :
        print('I am constructed')   # This is a constructor method that is called when an object is created
    # def __init__(self, z) :
    #     self.z = z
    #     print('I am constructed', self.z)   # This is a constructor method that is called when an object is created
        
    def party(self):
        self.x = self.x + 1
        print("So far", self.x)
    def __del__(self):
        print('I am destructed', self.x) # This is a destructor method that is called when an object is destroyed
an = PartyAnimal()

print("Type", type(an)) # type() shows the type of the object
print("Dir", dir(an)) # dir() shows the methods and attributes of the object
an.party() # So far 1
an.party() # So far 2`
an.party() # So far 3

# j = PartyAnimal("Jim")
# j.party() # So far 1  
# j.party() # So far 2 
# we can make new instances of the class and each instance has its own copy of the instance variables. the an and j objects are independent of each other. the x variable is stored in each object and is not shared.

# inheritance is a way to create a new class using classes that have already been defined. the new class is called a derived class and the one from which it inherits is called the base class.

class FootballFan(PartyAnimal): # FootballFan is a subclass of PartyAnimal
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.points, "points", self.x , "x")   
s = FootballFan()
s.touchdown() # So far 1 7 points 1 x