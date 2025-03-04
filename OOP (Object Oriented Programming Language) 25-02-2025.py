#OOP(Object Oriented Programming Language) - Object-oriented programming is a programming paradigm that is based on the concept of "objects", which can contain data and code that manipulates that data. In OOP, objects are created from templates called "classes", which define the properties and behavior of the objects they create.

#class Creation  - We define a class by using the 'class' keyword, followed by the class name and a colon, with the variables and methods in an indented block.A class is a code template for creating objects. Objects have member variables and have behaviour associated with them. In python a class is created by the keyword class . An object is created using the constructor of the class. This object will then be called the instance of the class.
'''
#1) Program :-  
class human():
    hair='black'
    height=7.2
    gender="male"
    def speak(self):
        return "i am speaking"
    def walk(self):
        return "i am walking"
person1=human()

print(person1.hair)
print(person1.height)
print(person1.gender)
print(person1.walk())
print(person1.speak())
#output :- black    
#          7.2
#          male
#          i am walking
#          i am speaking

#2) Program :- 
class tiger():
    hair='black and yellow'
    weight="139.7 kg"
    height="11 feet"
    Speed="49-65 km/h"
    habits_of_tigers="live alone and move chiefly at night."
    tigerbhai_ka_kam_dhana="hunt, eat, patrol their vast territories at night, and sleep during the day."
    gender="male"
    def tiger_asa_oradto(self):
        return "ekdam danger khu-khu karto"
    def tiger_kiti_tas_zoptos(self):
        return "bc mazi zop 20 tasachi "
    def tigerche_family_member(self):
        return "Mai,mere aai,baba aur pados wali"
    def tigerchi_Prajati(self):
        return "mazi 16 prajati ahe bc mlach nay mhit mi kuthlya jaaticha ahe "
    def tiger_kay_kam_karto(self):
        return "Mi dusryancha jiv swargat pohochavto"
        
animal1=tiger()

print(animal1.hair)
print(animal1.weight)
print(animal1.height)
print(animal1.Speed)
print(animal1.habits_of_tigers)
print(animal1.tigerbhai_ka_kam_dhana)
print(animal1.gender)
print(animal1.tiger_asa_oradto())
print(animal1.tiger_kiti_tas_zoptos())
print(animal1.tigerche_family_member())
print(animal1.tigerchi_Prajati())
print(animal1.tiger_kay_kam_karto())
#output :-  black and yellow
#           139.7 kg
#           11 feet
#           49-65 km/h
#           live alone and move chiefly at night.
#           hunt, eat, patrol their vast territories at night, and sleep during the day.
#           male
#           ekdam danger khu-khu karto
#           bc mazi zop 20 tasachi 
#           Mai,mere aai,baba aur pados wali
#           mazi 16 prajati ahe bc mlach nay mhit mi kuthlya jaaticha ahe 
#           Mi dusryancha jiv swargat pohochavto
'''
#3) Program :- 
name='raj'
class human:
    surname='kadam'
    def speak(self):
        return f"my is {name} and i am good"
master=human()
print(master.speak())
#output :-  my is raj and i am good