
""""

Computer does not know any thing about value.

First things you have to tell what is the type 

for eg 
10 - it is number 
Ansh - it is String 
21/05/2011 - date 
20.99 - Amount 

"""

op = input("Which operator >: ")
x = input("What is your first number >: ")
y = input("What is your second number >: ")

if op=="*":
    z = float(x) * float(y)
elif op=="+":
    z = float(x) + float(y)   
elif op=="-":
    z = float(x) - float(y)
elif op=="/":
    z = float(x) / float(y)            
else:
    print("We are working hard on adding support for " + op)
    z=0    
print( z)

