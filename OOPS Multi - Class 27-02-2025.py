'''
#1) Program :- 
class dad():
    money='2 lac'
    home='2 bhk'
    height=5.6
    def talk(self):
        return "my voice is hard"
    def walk(self):
        return "faster"
 
class mom():
    money=25000
    home='1 bhk'
    def talk(self):
        return "my voice is smooth"
    def walk(self):
        return "slower"
    def sleep(self):
        return "i am sleeping 4 hours"
    
class son(dad,mom):
    pass

obj=son()                       #IndentationError: expected an indented block after class definition on line 23
print(obj.money)                #AttributeError: 'son' object has no attribute 'money'    
print(obj.home)

#output :- 2 lac
#          2 bhk

#2) Program :- 
class dad():
    money='2 lac'
    home='2 bhk'
    height=5.6
    def talk(self):
        return "my voice is hard"
    def walk(self):
        return "faster"
 
class mom():
    money=25000
    home='1 bhk'
    def talk(self):
        return "my voice is smooth"
    def walk(self):
        return "slower"
    def sleep(self):
        return "i am sleeping 4 hours"
    
class son(mom,dad):
    pass

obj=son()                       
print(obj.money)                
print(obj.home)

#output :- 25000
#          1 bhk
'''
#3) Program :- 
class dad():
    money='2 lac'
    home='2 bhk'
    height=5.6
    def talk(self):
        return "my voice is hard"
    def walk(self):
        return "faster"
 
class mom():
    money=25000
    home='1 bhk'
    def talk(self):
        return "my voice is smooth"
    def walk(self):
        return "slower"
    def sleep(self):
        return "i am sleeping 4 hours"
    
class son(mom,dad):
    pass

obj=son()                       
print(obj.salary)                
