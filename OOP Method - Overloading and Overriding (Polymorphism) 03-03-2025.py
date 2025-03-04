#Polymorphism:- Polymorphism is a feature of object-oriented programming languages that allows a specific routine to use variables of different types at different times. Polymorphism in programming gives a program the ability to redefine methods for derived classes.

#Method of Polymorphism :-                                             
#1) Overloading :- Overloading. Method overloading is a form of polymorphism in OOP. Polymorphism allows objects or methods to act in different ways, according to the means in which they are used. One such manner in which the methods behave according to their argument types and number of arguments is method overloading.

#2) Overriding :- Overloading. Method overloading is a form of polymorphism in OOP. Polymorphism allows objects or methods to act in different ways, according to the means in which they are used. One such manner in which the methods behave according to their argument types and number of arguments is method overloading. 

#1) Program :- 
name='Kaustubh'
class dad():
    eye='black'
    nose='sharp'
    height=5.8
    def myself(self):
        return'Hi i am dad'
    
class mom():
    colour='black'
    hair='brown'
    salary=25000
    def myself(self):
        return 'Hi i am mom'
    
class son(dad,mom):
    def myself(self):
        return 'i am son'

#print(obj.name)
obj=son()
print(obj.nose)
print(obj.myself())
print(obj.salary)
print(name)
#output :-  sharp   
#           i am son
#           25000
#           Kaustubh