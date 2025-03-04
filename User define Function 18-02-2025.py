'''
#1) Program :- 
def fun(a,b=5,c):
    print(a+b+c)

fun(a=27,c=20)
#output :- SyntaxError: non-default argument follows default argument

#2)Program :- 
def fun(a,b=5,c=10):
    print(a+b+c)

fun(a=27,c=20)
#output :-    52

#3) Program :- 
def fun(a,b):
    print(a-b)

fun(-20,10)
#output :-  -30

#4) Program :-
def fun(a,b):
    print(a-b)

fun(b=-20,a=10)
#output :- 30

#5) Program :-
def fun(a=-20,b=40):
    print(a-b)

fun(b=-20,)
#output :- 0

#6) Program :-
def fun(a,b):
    print(f"Hi...! My name is {a} and my age is {b}")

fun('Neha',29)
#output :- Hi...! My name is Neha and my age is 29

#7) Program :- 
def fun(a,b):
    print(f"Hi...! My name is {a} and my age is {b}")

fun(29,'Mina')
#output :-  Hi...! My name is 29 and my age is Mina

#8) Program :- 
def fun(a,b):
    print(f"Hi...! My name is {a} and my age is {b}")               #f = Formula String

fun(29,a='Mina')
#output :- TypeError: fun() got multiple values for argument 'a'

#9) Program :-
def r(a=10,b=20,c=30):
    print(sum(a,b,c))

r(15,20,25)
#output :- TypeError: sum() takes at most 2 arguments (3 given)

#10) Program :- 
def r(a=10,b=20,c=30):
    print(sum(a,b))

r(15,20,25)
#output :- TypeError: 'int' object is not iterable

#11) Program :- 
def r(a=10,b=20,c=30):
    print(f"{a-b}+{c}")

r(15,20,25)
#output :- -5+25

#12) Program :- 
def r(a=10,b=20,c=30):
    print(f"{(a-b)+c}")

r(15,20,25)
#output :- 20
'''
