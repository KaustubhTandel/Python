#Constructor - Constructors in Python is a special class method for creating and initializing an object instance at that class. Every Python class has a constructor; it's not required to be defined explicitly. The purpose of the constructor is to construct an object and assign a value to the object's members.

#1) Program :-
name='raj'
age=25
class man():
    gender='male'
    def __init__(self,name):     #init(initialize) is a constructor
        self.name=name
    def display (self):
        return f"my name is {self.name}"
    
obj=man("ratan")
print(obj.display())

#output :-   my name is ratan

#2)Program :-
# name=mangabai
# age=99
class maid():
    gender='transgender'
    kam='laadi_pusne'
    def __init__(self,name,gender,kam):
        self.name=name
        self.gender=gender
        self.kam=kam
    def his_work (self):
        return f"my name is {self.name}and i am {self.gender} and ani maz kam ahe {self.kam}"
    
obj=maid("mungalabai","transgender","laadi_pusne")
print(obj.his_work())

#output :- my name is mungalabaiand i am transgender and ani maz kam ahe laadi_pusne

#3) Program :- 
age=30
class char():
    gender='male'
    def __init__(self,age):     #init(initialize) is a constructor
        self.age=age
    def COA (self):
        self.age=self.age-5
    
obj=char(25)
print(obj.COA())
print(obj.age)
#output :-  20

# Second Way :- 
age=30
class char():
    gender='male'
    def __init__(self,age):     #init(initialize) is a constructor
        self.age=age
    def COA (self):
        self.age=self.age-5
        return self.age
    
obj=char(25)
print(obj.COA())
#output :-  20







    
