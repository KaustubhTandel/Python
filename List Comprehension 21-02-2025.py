#List Comprehension :-   In Python, list comprehension is a method or construct that can be used to define and create a list from a string or another existing list. Besides creating lists, we can filter and transform data using list comprehension, which has a more human-readable and concise syntax.

#1) Ptogram:- 
a=[5,2,6,7]
b=[x*2 for x in a]
print(b)
#output :- [10, 4, 12, 14]

#2) Program :- 
a=[5,2,6,7]
b=[x*2 for x in a]
print(b)
c=[x for x in a if x%2==0]
print(c)
#output :-    [10, 4, 12, 14]   
#             [2, 6]

#3) Prohram :- 
m=[147,47,14,15,41,39]
d=[x for x in m if x%3==0 if x%7==0]
print(d)
#output :- [147]

#Second Way :- 
m=[147,47,14,15,41,39]
d=[x for x in m if x%3==0 elif x%7==0 else]   #We can not ladder in this program 
print(d)
#output :- SyntaxError: invalid syntax

#4) Program :- 
a=(list(range(2001,2025)))
c=[x for x in a if (x%400==0 or (x%4==0 and x%100!=0)) ]         
print(c)               
#output :-     [2004, 2008, 2012, 2016, 2020, 2024]

#5) Program :- 
a=[3,4,7,8]
c=[4/3*3.14*(x**3) for x in a ]
print(c)
#output :- [113.03999999999999, 267.94666666666666, 1436.0266666666666, 2143.5733333333333]

#6) Program :- 
base=2
height=[1,2,7,9]
area=[(1/2)*base*x for x in a]
print(area)
#output :- [3.0, 4.0, 7.0, 8.0]