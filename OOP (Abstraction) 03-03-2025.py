  #Abstraction :- Abstraction, in the context of OOP, refers to the ability to hide complex implementation details and show only the necessary features of an object. This simplifies the interaction with objects, making programming more intuitive and efficient.
'''
#1) Program :- 
class raj():
    a=10
    _b=20
    __c=30

obj=raj()
print(obj.a)     #It is a Public"
print(obj._b)    #It is a Protected"
print(obj.__c)   #AttributeError: 'raj' object has no attribute '__c'  "It is a Private"
# Output :-   10
#             20
#             AttributeError: 'raj' object has no attribute '__c' 

#2) Program :- 
class raj():
    a=10
    _b=20
    __c=30
    def art(self):
        return f"{self.__c}"
obj=raj()
print(obj.a)     
print(obj._b)
print(obj.art())
# Output :-     10
#               20
#               30

#3) Program :- 
class raj():
    a=10
    _b=20
    __c=30
    def art(self):
        self.__c=self.__c-5
        return f"{self.__c}"
obj=raj()
print(obj.a)     
print(obj._b)
print(obj.art())
#output :-    10
#             20
#             25
'''
#4) Program :- 
class garage():
    start_engine = "key"
    _stop_engine = "poweroff"
    __petrol = "0.5Ltr"
    def Royale(self):
        return f"{self._stop_engine}"
    def Royale1(self):
        return f"{self.__petrol}"
obj=garage()
print(obj.Royale())
print(obj.Royale1())
#output :-    poweroff
#             0.5Ltr