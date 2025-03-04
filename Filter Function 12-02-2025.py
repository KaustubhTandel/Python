# Filter Function :- The Python filter() function is a built-in function that allows you to filter a sequence (e.g., a list, #                    tuple, or set) based on a given condition. The function takes two arguments – a function and a sequence – and #                    returns an iterator containing elements from the original sequence for which the function returns True.


#1) Program :- 
a=['raj', 'mani', (), 'niddda']
b=(list(filter(None,a)))        #It takes only None,not none,null,0 or other.
print(b)
#output :- ['raj', 'mani', (), 'niddda']

#2) Program :- 
a=['raj', 'mani', (), 'niddda']
b=(list(filter(0,a)))
print(b)
#output :- TypeError: 'int' object is not callable