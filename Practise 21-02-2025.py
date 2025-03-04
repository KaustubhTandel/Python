'''
#1) Program :-
a=(1,2,3,4,5,1,2,3,4,5,1,2,5)
b=tuple(a)
c=set(b)
d=list(a)
a=c
print(a)
print(type(a))
#Output :-    {1, 2, 3, 4, 5}
#             <class 'set'>

#2) Program :-
a=(1,2,3,4,5,1,2,3,4,5,1,2,5)
b=tuple(a)
c=set(b)
d=list(a)
a=d
print(a)
print(type(a))
#output :-    [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 5]
#              <class 'list'>  

#3) Program :-
a=(1,2,3,4,5,1,2,3,4,5,1,2,5)
c=sorted(list(tuple(set(a))))
print(c)
#output :-     [1, 2, 3, 4, 5]

#4) Program :- 
a=2
for i in range(a-1,6):
    print(a,end="f{a}")
print("roshni")
#output :- 2f{a}2f{a}2f{a}2f{a}2f{a}roshni

#5) Program :-
a='nida'
for i in a:
    print('nida',end="khan")
#output :-   nidakhannidakhannidakhannidakhan

#6) Program :-
a='nida'
for i in range(len(a)):
    print('N',end=f'{sorted(a)}')
#output :- N['a', 'd', 'i', 'n']N['a', 'd', 'i', 'n']N['a', 'd', 'i', 'n']N['a', 'd', 'i', 'n']

#7) Program :- 
a='nida'
for i in range(len(a)):
    print('N',end=f'{(a)}')
#output :- N['a', 'd', 'i', 'n']N['a', 'd', 'i', 'n']N['a', 'd', 'i', 'n']N['a', 'd', 'i', 'n']NnidaNnidaNnidaNnida

#8) Ptogram:- 
a=5
b=[a for i in range(1,a):print('r')]
#output :-    SyntaxError: invalid syntax

#9) Ptogram:- 
a=[5,2,6,7]
b=[a for i in range(1,a):print('r')]
#output :-   SyntaxError: invalid syntax
'''

