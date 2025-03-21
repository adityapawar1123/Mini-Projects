#Welcome to world's most inefficient way of making a basic calculator
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

c = input("What do you want me to do? ")
if c == "add" : print(a+b)
elif c == "Add" : print(a+b)
elif c == "Addition" : print(a+b)
elif c == "addition" : print (a+b)

elif c == "subtract" : print (a-b)
elif c == "subtraction" : print (a-b)
elif c == "Subtraction" : print (a-b)
elif c == "Subtract" : print (a-b)

elif c == "Multiply" : print (a*b)
elif c == "multiply" : print (a*b)
elif c == "multiplication" : print (a*b)
elif c == "Multiplication" : print (a*b)

elif c == "divide" : print (a/b)
elif c == "Divide" : print (a/b)
elif c == "Division" : print (a/b)
elif c == "division" : print (a/b)
else : print("Cant do that operation")