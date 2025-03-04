
#Found a reverse number with the hepl of While loop...?
n=int(input('enter the number :- '))
rev=0
while (n>0):
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
print(rev)
#output :- enter the number :- 1234
#          4321

a=1//10
print(a)