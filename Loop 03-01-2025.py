
# 1) Program :- 
a=range(1,5)
print(a)
#Output - range(1,5)

# 2) Program :- 
a=tuple(range(1,5))
print(a)
#Output - (1, 2, 3, 4)

# 3) Program :- 
a=tuple(range(5,0,-1))
print(a)
#Output - (5, 4, 3, 2, 1)

# 4) Program :- 
a=(tuple(5,0,-1))
print(a)
#Output - tuple expected at most 1 argument, got 3

# 5) Program :-
r="rajendra sir is the best"
q=r[0:8:1]+" "+r[-4: :1]
print(q)
#Output - rajendra sir 

# 6) Program :-
a=tuple(range(1,-10,-1))
print(a)
#output - (1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9)

# 7) Program :-


# 8) Program :-
a=set(range(1,6,1))
print(a)
print(type(a))
#output - {1, 2, 3, 4, 5}
#         <class 'set'>

# 9) Program :-
#[1,-1,-3,-5] output pahije same 
a=list(range(1,-6,-2))
print(a)
#output - [1, -1, -3, -5]

# 10) Program :-
for i in range(1,11,1):
    print(i)
#output - 1
#         2
#         3
#         4
#         5
#         6
#         7
#         8
#         9
#         10

# 11) Program :-
for i in range(1,11,1):
    print("rajendra")
#output - rajendra
#         rajendra
#         rajendra
#         rajendra
#         rajendra
#         rajendra
#         rajendra
#         rajendra
#         rajendra
#         rajendra

# 12) Program :-
for i in range(1,11,1):
    print(i)
    print(i+1)
#output - 1
#         2
#         2
#         3
#         3
#         4
#         4
#         5
#         5
#         6
#         6
#         7
#         7
#         8
#         8
#         9
#         9
#         10
#         10
#         11

# 13) Program :-
for i in range(1,11,1):
    print(i)
    print(i+1)
    print(tuple(i+1))
#output - 1
#         2
#  'int' object is not iterable  

# 14) Program :-
for i in range(6,1,-1):
    print(i-1)
#output - 5
#         4
#         3
#         2
#         1

# 15) Program :-
a=1
for i in range(6-a,1-a,-1):
    print(i)
#output - 5
#         4
#         3
#         2
#         1

print(chr(65)) #A la default ahe value
print(chr(95)) #_ la default ahe value

# 16) Program :-
for i in range(7,1,-1):
    print("*")
#output - *
#         *
#         *
#         *
#         *
#         *

# 17) Program :-
for i in range(1,51,1):
    print(chr(65+i))
'''
#output - B
#         C
        D
E
F
G
H
I
J
K
L
M
N
O
P
Q
R
S
T
U
V
W
X
Y
Z
[
\
]
^
_
`
a
b
c
d
e
f
g
h
i
j
k
l
m
n
o
p
q
r
s
'''