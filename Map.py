#Map Function :- Map in Python is a function that works as an iterator to return a result after applying a function to every item of an iterable (tuple, lists, etc.). It is used when you want to apply a single transformation function to all the iterable elements.
'''
#1) Program :- 
a=[5,4,3,2,1,]
def palin(n):
    n1=n
    rev=0
    while n>0:
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    if n1==rev:
        print(f"{n1}",end=" ")
    else:
        print('not palin',end=" ")
a=list(map(palin,sorted(a)))
#output :- 1 2 3 4 5

#2) Program :- 
a=[112,252,121,412]
def palin(n):
    n1=n
    rev=0
    while n>0:
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    if n1==rev:
        print(f"{n1}",end=" ")
    else:
        print('not palin',end=" ")
a=list(map(palin,sorted(a)))
#output :- not palin 121 252 not palin

#3) Program :- 
def fun(a,b=5,c):
    print(a+b+c)

fun(a=27,c=20)
#output :- SyntaxError: non-default argument follows default argument

#4)Program :- 
def fun(a,b=5,c=10):
    print(a+b+c)

fun(a=27,c=20)
#output :-    52
'''
#5) Program :- 
def fun(a,b):
    print(a-b)

fun(-20,10)
#output :-  -30