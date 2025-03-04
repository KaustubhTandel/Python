#1) how to find volume of sphere in given number ?
# list = (1,2,3,6,5)
# def volumeofsphere():
#     radius=int(input("enter the radius :-   "))
#     volume=(4/3)*(22/7)*radius*radius*radius      
#     print(f'volume of sphere is cubic units')
# volumeofsphere()

#2) Find the Palindrome Of given function ? 
# Palindrome :- A number that is unchanged when the number or digits are reversed is known as a palindrome number in Python. For   example, the palindrome numbers are 131, 22, 515, 2332, and 84848.
x=(1,101,102,111,10,141,2)
def palin(n):
    n1=n
    rev=0
    while n>0:
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    if n1==rev:
        print('palin')

palin(101)
#output :- palin

#3) Program :- 
x=(1,101,102,111,10,141,2)
def palin(n):
    n1=n
    rev=0
    while n>0:
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    if n1==rev:
        print('palin')
    else:
        print('not palin')
a=list(map(palin,x))
print(a)
#output :-   palin
#            palin
#            not palin
#            palin
#            not palin
#            palin
#            palin
#            [None, None, None, None, None, None, None]

#4) Show the output in horizontal line ?
#  Program :- 
x=(1,101,102,111,10,141,2)
def palin(n):
    n1=n
    rev=0
    while n>0:
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    if n1==rev:
        print('palin',end=" ")
    else:
        print('not palin',end=" ")
a=str(map(palin,x))
print(a)
#output :- palin palin not palin palin not palin palin palin [None, None, None, None, None, None, None]

#5) Program :- 
x=(1,101,102,111,10,141,2)
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
a=list(map(palin,x))
print(a)
#output :- 1 101 not palin 111 not palin 141 2 [None, None, None, None, None, None, None]
