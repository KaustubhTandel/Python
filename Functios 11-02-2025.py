#Function :- A called function performs a defined task and when its return statement is executed or when its function-ending closing brace is reached, it returns the program control back to the main program.

#The another name of function are :- 

#1) Predefine Function :- A predefined function is a function that has already been written in the programming language and can be used by the programmer. A function will return a value that can be stored in a variable or sometimes in a conditional statement.

#2) In-Build Function :- Built-in functions are the pre-defined function in Python that allows using the basic properties of string and numbers in your rules. There are 60+ built-in functions in Python. The top 10 built-in functions are abs, chr, dict, enumerate, float, len, list, ord, range, and set.

#1) Program :- 
def sachin():
    a=int(input("enter 1st number :- "))
    b=int(input("enter 2nd number :- "))
    c=int(input("percentage :- "))
    final=(a+b)*c/100
    print(final)


sachin()
#output :-    enter 1st number :- 22
#             enter 2nd number :- 24
#             percentage :- 10
#             4.6

#2) Program :- 
def nida(a,b,c):
    final=(a+b)*c/100
    print(final)

nida(22,24,10)
#output :-   4.6

#3) Program :- 
def deaf(n):
    rev=0
    while (n>0):
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    print(rev)

deaf(8866)
#output :-   8866

#4) Program :-
def greet(a):
    print("holla sachin a")

greet()
#output :-     TypeError: greet() missing 1 required positional argument: 'a'

#5) Program :-
def greet(a):
    print("holla user",a)

greet("Kaustubh")
#output :-    holla user Kaustubh

#6) Program :-
def greet(a):
    print(f"holla user {a}")      #f is a Formula String (it's help to run formula in string)

greet("Kaustubh")
#output :-      holla user Kaustubh

#7) Program :-   
def greet():
    a=str(input("enter the name :- "))
    print(f"holla user {a}")      # f is a Formula String (it's help to run formula im string)

greet()
#output :-    enter the name :- Kaustubh
#             holla user Kaustubh

#8) Program :-
def berojgaar():
    pagar=int(input("Krupaya tumcha pagar sanga :-  "))
    kaplela_pf=int(input("Krupaya tumcha pf sanga :-   "))
    kaplela_esic=int(input("Krupaya tumcha espi sanga :-     "))
    dhoganche_addition=(kaplela_pf+kaplela_esic)
    haatat_alela_pagar=pagar*dhoganche_addition/100
    print(haatat_alela_pagar)
berojgaar()
#output :-     Krupaya tumcha pagar sanga :-  12000
#              Krupaya tumcha pf sanga :-   12
#              Krupaya tumcha espi sanga :-     8
#              2400.0

#9) Program :-  
#First way :- 
def volumeofsphere():
    radius=int(input("enter the radius :-   "))
    volume=(4/3)*(22/7)*radius*radius*radius              #using formula of volume of sphere
    print(f'volume of sphere is {volume} cubic units')
volumeofsphere()
#output :-     enter the radius :-   8
#              volume of sphere is 2145.523809523809 cubic units

#Second way :- 
def volumeofsphere():
    radius=int(input("enter the radius :-   "))
    volume=(4/3)*(22/7)*(radius**3)
    print(f'volume of sphere is {volume} cubic units')
volumeofsphere()
#output :-     enter the radius :-   8
#              volume of sphere is 2145.523809523809 cubic units

