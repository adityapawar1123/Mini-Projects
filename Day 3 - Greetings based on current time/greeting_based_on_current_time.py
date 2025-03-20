from datetime import datetime
#When we use from we use only one class of datetime, if we use import only then
#we import entire library of datetime to it
#if we use import datetime we'll need to write like :
# time = datetime.datetime.now()

time = datetime.now().hour
a = input("Hey! What's your name? ")
if 6 <= time <= 12 : print(f"Good morning {a}")
elif 12 <= time <= 17 : print(f"Good afternoon {a}")
elif 17 <= time <= 23 : print(f"Good evening {a}")
else : print(f"Ayyy {a} looks like you're a night owl")