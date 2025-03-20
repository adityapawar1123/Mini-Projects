import pyttsx3
engine = pyttsx3.init()

engine.say("Hey there! Please enter your first number")
engine.runAndWait()
a = int(input("Enter 1st number : "))

engine.say("What do you want me to do with this number?")
engine.runAndWait()

q1 = input("What do you want me to do with this number?")
if q1.lower() in ["square it" ,"square", "raise power to 2"] : 
  engine.say(f"The square of {a} is {a**2}")
  engine.runAndWait()
  print(f"The square of {a} is {a**2}")

elif q1.lower() in ["square root", "root", "what's its root", "what's its square root"] :
  square_root = f"The square root of {a} is {a**0.5}"
  engine.say(square_root)
  engine.runAndWait()
  print(square_root)

elif q1.lower() in ["increase its power", "exponent", "raise to power"] : 
  engine.say("Enter the power")
  engine.runAndWait()
  p = int(input("Enter the power : "))
  power = f"The answer for {a} raise to the power {p} is {a**p}"
  engine.say(power)
  engine.runAndWait()
  print(power) 

else : 
  
 engine.say("Please enter your second number")
 engine.runAndWait()
 b = int(input("Enter 2nd number : "))

 engine.say("What do you want me to do with these 2 numbers?")
 engine.runAndWait()
 q2 = input("What do you want me to do with these 2 numbers?")

 if q2.lower() in ["add", "addition", "add numbers", "add them", "i want you to add them"] :
  sum = f"The sum of {a} and {b} is {a+b}"
  engine.say(sum)
  engine.runAndWait()
  print(sum)

 elif q2.lower() in ["subtract", "subtraction", "subtract numbers", "subtract them", "i want you to subtract them"] : 
   subtract = f"The difference of {a} and {b} is {a-b}"
   engine.say(subtract)
   engine.runAndWait()
   print(subtract)

 elif q2.lower() in ["multiply", "multiplication", "multiply them", "i want you to multiply them"] :
   multiply = f"The product of {a} and {b} is {a*b}"
   engine.say(multiply)
   engine.runAndWait()
   print(multiply)

 elif q2.lower() in ["divide", "division", "divide them", "i want you to divide them"] : 
   if b != 0 :
      divide = f"The quotient of {a} and {b} is {a/b}"
      engine.say(divide)
      engine.runAndWait()
      print(divide)
   else : 
      error = "Division by zero is not possible."
      engine.say(error)
      engine.runAndWait()
      print(error)

 elif q2.lower() in ["remainder", "remainder of", "division remainder", "what's their remainder"] :
   if b != 0 : 
      remainder = f"The remainder of {a} and {b} is {a%b}"
      engine.say(remainder)
      engine.runAndWait()
      print(remainder)
   else : 
    error2 = "Division by zero is not possible, so I can't give you a remainder."
    engine.say(error2)
    engine.runAndWait()
    print(error2)

 else :
   engine.say("I can't perform that operation.")
   engine.runAndWait()
   print("I can't perform that operation.")