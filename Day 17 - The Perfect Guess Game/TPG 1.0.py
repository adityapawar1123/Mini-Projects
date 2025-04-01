import random 


print("Hey there, the game starts now!")

while True :
 a = random.randint(0, 100)
 guessNo= 0
 
 while True : 
    n = int(input("Guess the number : "))

    if  a==n : 
        guessNo += 1
        print(f"Your guess was right! The answer is {n}\nNumber of guesses = {guessNo}")
        break
        
    elif n<a : 
        print(f"Wrong guess\nPick a higher number than {n}")
        guessNo+=1

    elif n>a : 
        print(f"Wrong guess\nPick a lower number than {n}")
        guessNo+=1

 loop_question = input(("Wanna play one more game?(yes/no) : "))

 if loop_question.lower().strip() not in ["yes", "y"] : 
    print("Okay have a good day")
    break

