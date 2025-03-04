#Lambda function :- A lambda function is an anonymous function (i.e., defined without a name) that can take any number of         arguments but, unlike normal functions, evaluates and returns only one expression.

#1) Program :- 
a=10
b=20
m=lambda a,b:a+b
print(m(10,20))
#output :- 30

#2) Program :-
a=10
b=20
c=30
m=lambda a,b,c:a*b*c
print(m(10,20,30))
#output :- 6000

#3) Program :- 
m=lambda a,b:a>b
print(m(10,20))
#output :- False 

#4) Program :- 
m=lambda a,b:a in b
print(m(10,20))
#output :- TypeError: argument of type 'int' is not iterable

#5) Program :- 
m=lambda a,b:a in b
print(m(10,(10,20,30)))
#output :- True

#6) Program :- 
m=lambda a,b:30 is b
print(m(10,(10,20,30)))
#output :- SyntaxWarning: "is" with a literal. Did you mean "=="?
#          m=lambda a,b:30 is b
#          False

#7) Program :- 
m=lambda a,b:a is b
print(m(10,10))
#output :- True

#8) Program :- 
m=lambda a,b,c:a is b in c
print(m(10,10,(0.10,'10',10.00,10)))
#output :- True



