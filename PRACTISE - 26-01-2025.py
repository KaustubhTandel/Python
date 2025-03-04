'''
#1. Program to print maximum among two numbers. 
a=5
b=10
print(max(a,b))

#2. Program to print maximum among three numbers.
a=15
b=35
c=100
print(max(a,b,c))

#3. Program to check whether a given number is divisible by 3 or not.
a=int(input("enter the number = "))
if a%3==0:
    print("Yes it is divisible by 3")
else:
    print("No it's not divisible by 3")

#4. Program to check whether a given number is divisible by 5 or not.
a=int(input("enter the number = "))
if a%5==0:
    print("yes divisible by 5")
else:
    print("invalid number")

#5. Program to check whether a given number is divisible by 11 or not.
a=int(input("enter the number = "))
if a%11==0:
    print("divisble by 11")
else:
    print("invalid number")

#6. Program to check whether a given number is even or odd.
a=int(input("emter the number =  "))
if a%2==0:
    print("it is a even number")
else:
    print("it is a odd number")

#7. Program to check whether a year is a leap year or not.
a=int(input("enter the year = "))
if a%400==0 and (a%4 or a%100==0):
    print("it is a leap year")
else:
    print("it is not a leap year")
'''
#8. Program to check whether a given input is digit or not. - no answer
#9. Program to check whether a given input is the alphabet or not.
a=complex(input("enter the alphabet =  "))
ch='z'
if 'a'<=ch<='z'  'A'<=ch<='Z':
    print("the alphabet ",ch,"is a alphabet")
else:
     print("the alphabet ",ch,"is not an alphabet")
