'''
This is not what harry (the tutorial) made
I made this by myself where computer has random inputs
If you wanna watch his project then go on yt
Both projects are pretty similar but u can analyse win/lose moements in his project as he used
-1,0,1 for convention of rock,paper,scissors 
'''


import random 
print("Hey! Let's play a game of rock paper scissors!")

while True : 
    list = ["Rock", "Paper", "Scissors"]
    list_random = random.choice(list)

    user = input("Choose (rock/paper/scissors) : ")

    computer_chose = list_random

    def ending_msg(n) :
        print(f"You chose : {n}\nComputer chose : {computer_chose}")

    if user.lower().strip() in ("r", "rock") :
        
        if computer_chose == "Paper" :
            print("You lost!")
            ending_msg("Rock")
        elif computer_chose == "Rock" :
            print("It's a draw!")
            ending_msg("Rock")
        else : 
            print("You won!")
            ending_msg("Rock")


    elif user.lower().strip() in ("s", "scissors", "scissor") :
        
        if computer_chose == "Paper" :
            print("You won!")
            ending_msg("Scissors")
        elif computer_chose == "Rock": 
            print("You lost!")
            ending_msg("Scissors")
        else : 
            print("It's a draw!")
            ending_msg("Scissors")


    elif user.lower().strip() in ("p", "paper")  :
        if computer_chose == "Paper" :
            print("It's a draw")
            ending_msg("Paper")
        elif computer_chose == "Rock" : 
            print("You won!")
            ending_msg("Paper")
        else : 
            print("You lost!")
            ending_msg("Paper")

    else : 
        print("That's invalid")
    
    loop_q = input("Wanna play another?(yes/no) : ")
    if loop_q.lower().strip() not in ["yes", "y", "yess"] :
        print("Okay, have a good day!")
        break