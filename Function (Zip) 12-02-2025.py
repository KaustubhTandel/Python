#Zip Function :-   The zip() function in Python is a neat tool that allows you to combine multiple lists or other iterables (like #                  tuples, sets, or even strings) into one iterable of tuples. Think of it like a zipper on a jacket that brings #                  two sides together.

#1) Program :- 
a=[1,2,3,4,5]
b=['a','b','c','d']
print(zip(a,b))
#output :-  <zip object at 0x7f5c0c82d000>

#2) Program :-
a=[1,2,3,4,5]
b=['a','b','c','d']
print(list(zip(a,b)))
#output :-   [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

#3) Program :- 
a=[1,2,3,4,5]
b=['a','b','c','d']
print(dict(zip(a,b)))
#output :-  {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

#4) Program :- 
a=[1,2,3,4,5]
b=['a','b','c','d']
c={5,6,7,8,9}
print(dict(zip(b,c)))
#output :- {'a': 5, 'b': 6, 'c': 7, 'd': 8}

#5) Program :- 
a=[1,2,3,4,5]
b=['a','b','c','d']
c={5,6,7,8,9}
print(dict(zip(c,b)))
#output :-  {5: 'a', 6: 'b', 7: 'c', 8: 'd'}

#6) Program :- 
a=[1,2,3,4,5]
b=['a','b','c','d']
c={5,6,7,8,9}
for i in zip(a,b):
    print(i)
#output :- (1, 'a')
#          (2, 'b')
#          (3, 'c')
#          (4, 'd')

#7) Program :- 
a=()
for i in zip(a,b):
    a.update(i)
print(a)
#output :-  ()

#8) Program :- 
a=[1,2,3,4,5]
b=['a','b','c','d']
c={5,6,7,8,9}
a=list()
for i in zip(a,):
    a.update(i)
print(a)
#output :- []

#9) Program :- 
a=[1,2,3,4,5]
b=['a','b','c','d']
c={5,6,7,8,9}
a=[]
for i in range(1,15):
    print(a.update(i))
#output :-  AttributeError: 'list' object has no attribute 'update'

#10) Program :- 
a={'a':1,'b':2,'c':3}
b=[1,2,3]
print(tuple(zip(a,b)))
#output :-  (('a', 1), ('b', 2), ('c', 3))

#11) Program :- 
a={'a':1,'b':2,'c':3}
b=[1,2,3]
print(tuple(zip(b,a)))
#output :-  ((1, 'a'), (2, 'b'), (3, 'c'))

#12) Program :- 
a=['raj',"","",'mani',(),'niddda']
a.remove("")
a.remove('')
print(a)
#output :-   ['raj', 'mani', (), 'niddda']

