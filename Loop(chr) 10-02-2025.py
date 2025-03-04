'''
#1) Program :- 
a=5
for i in range(1,a):
    for j in range(0,a-1):
        print(chr(97+j),end=" ")
    print()
#output :-  a b c d 
#           a b c d 
#           a b c d 
#           a b c d

#2) Program :- 
a=5
for i in range(1,a):
    for j in range(0,a-1):
        print(chr(65+j),end=" ")
    print()
#output :-   A B C D 
#            A B C D 
#            A B C D 
#            A B C D.
# 
#3) Program :-
a=5
for i in range(1,a):
    for j in range(i-1,3+i):
        print(chr(97+j),end=" ")
    print()
#output :-   a b c d 
#            b c d e 
#            c d e f 
#            d e f g
'''
#4) Program :- 
a=5
for i in range(1,a):
    for j in range(i-3,1+i):
        print(chr(97+j),end=" ")
    print()
#Reverse me karna hai 