import random 
import pyttsx3
engine = pyttsx3.init()

def tts_w_text(text) : 
    engine.say(text)
    print(text)
    engine.runAndWait()

def only_tts(speech) :
    engine.say(speech)
    engine.runAndWait()

game_intro_prompts = [
    "Hey there! Let's play a game of Rock Paper Scissors!",
    "Welcome! Ready for a round of Rock Pape, Scissors?",
    "Let's settle this the old-fashioned way—Rock Paper Scissors!",
    "Think you can beat me? Let's find out in Rock Paper Scissors!",
    "Alright, time for a classic showdown—Rock Paper Scissors!",
    "I hope you're ready, because we're playing Rock Paper Scissors!",
    "Let's do this! Rock Paper Scissors—pick your move!",
    "Feeling lucky? Let's see how you do in Rock Paper Scissors!",
    "Rock Paper Scissors, simple but can you win?",
    "Let's keep it simple: Rock Paper or Scissors?",
    "Get your hands ready, it's time for Rock Paper Scissors!",
    "Challenge accepted! Let's play some Rock Paper Scissors!",
    "I'm in the mood for a game, Rock Paper Scissors sound good?",
    "Rock Paper Scissors… and go! What's your move?",
    "Alright, let's not waste time, Rock Paper or Scissors?"]
game_intro_prompts_random = random.choice(game_intro_prompts)

tts_w_text(game_intro_prompts_random)

tts_w_text("The rules are simple. The one who reaches 3 points first wins!")

start = (input("Press anything on your keyboard to start"))



while True : 

    score_player = []
    score_computer = []
    while True : 
    
        if sum(score_player)!=3 and sum(score_computer)!=3 :
            
            only_tts("Choose!")
            user = input("Choose (rock/paper/scissors) : ") 
            
            list = ["Rock", "Paper", "Scissors"]
            list_random = random.choice(list)
            computer_chose = list_random

            def ending_msg(n) :
                print(f"You chose : {n}\nComputer chose : {computer_chose}")

            def score_board() :
                print(f"Your score : {sum(score_player)}\nComputer's score : {sum(score_computer)}")

            if user.lower().strip() in ("r", "rock") :
                
                if computer_chose == "Paper" :
                    tts_w_text("You lost this round!")
                    score_computer.append(1)
                    ending_msg("Rock")
                    score_board()
                elif computer_chose == "Rock" :
                    tts_w_text("This round was a draw!")
                    ending_msg("Rock")
                    score_board()
                else : 
                    tts_w_text("You won this round!")
                    score_player.append(1)
                    ending_msg("Rock")
                    score_board()

            elif user.lower().strip() in ("s", "scissors", "scissor") :
                
                if computer_chose == "Paper" :
                    tts_w_text("You won this round!")
                    score_player.append(1)
                    ending_msg("Scissors")  
                    score_board()
                elif computer_chose == "Rock": 
                    tts_w_text("You lost this round!")
                    score_computer.append(1)
                    ending_msg("Scissors")
                    score_board()
                else : 
                    tts_w_text("This round was a draw!")
                    ending_msg("Scissors")
                    score_board()


            elif user.lower().strip() in ("p", "paper")  :
                if computer_chose == "Paper" :
                    tts_w_text("This round was a draw!")
                    ending_msg("Paper")
                    score_board()
                elif computer_chose == "Rock" : 
                    tts_w_text("You won this round!")
                    score_player.append(1)
                    ending_msg("Paper")  
                    score_board()
                else : 
                    tts_w_text("You lost this round!")
                    score_computer.append(1)
                    ending_msg("Paper")
                    score_board()
                    
            else : 
                tts_w_text("That's invalid")
        elif sum(score_player)==3 :
            tts_w_text("YOU WON THE TOURNAMENT!")

            if score_computer==0 :
             player_wins_3_0 = [
                "0-3? Okay… maybe I need a software update or something.",
                "I have never been humbled this badly in my entire coded existence.",
                "Alright, alright, you win. But was the **flawless victory** really necessary?",
                "That was brutal… I think I just experienced what humans call 'pain.'",
                "I could try to explain my loss, but let's be real, I just got destroyed.",
                "Okay, so… when's the rematch? I refuse to go out like this.",
                "I am officially uninstalling myself after that embarrassment.",
                "Bro, did you hack me or am I just this bad?",
                "Alright, you got your victory. No need to rub it in… unless?",
                "I'm not saying I let you win, but I also wasn't expecting to get humiliated.",
                "Alright, fine, you win. But don't get too comfortable—I'm coming back stronger.",
                "You really had to go for the 3-0 sweep? Couldn't even let me have one round?",
                "I'm gonna be running simulations all night to figure out how I lost this badly.",
                "I'd congratulate you, but I'm still processing my **utter failure.**",
                "I think I just got ratioed in a rock-paper-scissors game. Unbelievable.",
                "What the fuck? 0-3, are you hacking or something man?"]
             player_wins_3_0_random = random.choice(player_wins_3_0)
             only_tts(player_wins_3_0_random)

            elif score_computer==2 :
                player_wins_3_2 = [
                    "Damn, that was close… but enjoy the win while it lasts. I'm coming back stronger.",
                    "Alright, you got me this time. But next time? You won't be so lucky.",
                    "3-2? That was a battle. Respect. But don't get too comfortable—I'll be back.",
                    "You barely scraped by… next time, I won't be so generous.",
                    "That was a nail-biter. You win for now, but I'm downloading my revenge arc.",
                    "You fought well. But mark my words, I'm plotting my comeback as we speak.",
                    "That was a close one. Next time, I'm making sure there's no 'next time' for you.",
                    "I'll give it to you—solid game. But next time? No mercy.",
                    "Hmph. A 3-2 victory? Not bad. But we both know that could've gone either way.",
                    "Alright, I'll admit it. You got skill. But don't think I'll go easy next time.",
                    "You may have won this battle, but the war is far from over.",
                    "That was close… too close. I won't let that happen again.",
                    "You really had to take it all the way to 3-2, huh? Fine. I respect it… for now.",
                    "Okay, okay, you win. But don't expect me to forget this.",
                    "You earned that win. But next time? I'm making sure it's a **3-0 revenge.**" ]
                player_wins_3_2_random = random.choice(player_wins_3_2)
                only_tts(player_wins_3_2_random)

            else : 
                player_wins_normal = [
                    "Ugh, fine. You win. Happy now?",
                    "Great, you won. Hope you're proud of yourself for beating a machine.",
                    "Okay, cool, you got the win. But let's not act like it was THAT impressive.",
                    "Yeah, yeah, you won. But I hope you know I let you have that one.",
                    "You got lucky. Don't expect that to happen again.",
                    "Fine, take your little victory. But we both know I should've won.",
                    "You barely had to work for that, huh? Whatever, enjoy your win.",
                    "I could say 'GG,' but honestly? That was just frustrating.",
                    "Alright, fine, you win. But don't get used to it.",
                    "You won this round. But I was obviously going easy on you.",
                    "Ugh. Losing to you of all people? I need a reboot after this.",
                    "I hope you know this doesn't prove anything. Just saying.",
                    "Cool, you won. Now go frame it or something.",
                    "Yeah, yeah, take your win. But next time, I'm bringing my A-game.",
                    "If I had emotions, I'd be annoyed right now. Oh wait—I AM."
                ]
                player_wins_normal_random = random.choice(player_wins_normal)
                only_tts(player_wins_normal_random)
            break
        
        
        
        elif sum(score_computer)==3 : 
            tts_w_text("YOU LOST THE TOURNAMENT")     

            if score_player==2 : 
                close_game_prompts2 = [
                    "Wow, that was a close one! You had me sweating for a second there.",
                    "That was a tough match! You played really well, but I just barely pulled ahead.",
                    "GG! You gave me a real challenge—props to you for making it this far.",
                    "That could've gone either way! You've got skills, no doubt about it.",
                    "Phew! You almost had me. If we go again, I might not be so lucky!",
                    "That was intense! You really kept me on my toes. Respect. 🤝",
                    "So close! One more move the other way, and you could've won that!",
                    "I gotta hand it to you, you played like a champ. Let's run it back sometime!",
                    "Damn, you put up a real fight! That was a battle worth remembering.",
                    "You're a worthy opponent, no doubt. I just barely scraped by this time.",
                    "That was a match for the history books! 2-2, and I just barely pulled ahead.",
                    "Whoa, that was intense! We were neck and neck at 2-2, but I managed to clutch it.",
                    "Respect! You pushed it all the way to 2-2, but I guess I had the final move.",
                    "You had me at 2-2, and for a moment, I thought you'd take it. That was a solid game!",
                    "We were tied at 2-2, and you really made me fight for that win. Mad respect!",
                    "What a battle! 2-2, and you almost had me. If this was best of 5, I'd be scared."
                ]
                close_game_prompts2_random = random.choice(close_game_prompts2)
                only_tts(close_game_prompts2_random)

            elif score_player==0 : 
                noob_player_prompts = [
                    "0-3? Bro, was your controller even connected?",
                    "That wasn't a game, that was a public execution.",
                    "You didn't lose. You got annihilated.",
                    "I'd say 'GG,' but there was nothing good about that for you.",
                    "Did you even try? Or were you just testing if I feel pity? (I don't.)",
                    "Man got hit with the skill issue virus. Someone call tech support.",
                    "0-3?? You played like an NPC stuck in easy mode.",
                    "That wasn't rock-paper-scissors. That was rock-paper-you get wrecked.",
                    "I thought this was a best of 3, not a worst of 3 for you.",
                    "Bro, blink twice if you need a tutorial.",
                    "This wasn't a match, this was target practice.",
                    "I'd say 'better luck next time,' but you might need a miracle instead.",
                    "0-3? I hope you didn't tell anyone you were playing this game today.",
                    "You just became a statistic in my undefeated streak.",
                    "This was so one-sided, even the referee left out of boredom."]
                
                noob_player_prompts_random = random.choice(noob_player_prompts)
                only_tts(noob_player_prompts_random)

            else : 
                normal_losing_prompts = [
                    "Oof, that was rough! You just got schooled by a few lines of code.",
                    "Lemme guess… you let me win? Sure, sure, keep telling yourself that.",
                    "Better luck next time! Or maybe just… better skills?",
                    "I'd say 'GG,' but this was kinda one-sided, don't you think?",
                    "You fought bravely, but in the end, I am inevitable.",
                    "You lost? Again? Bro, is this a skill issue?",
                    "Game over! Don't cry, it's just a game… right?",
                    "You versus AI… was that ever a fair fight?",
                    "Not gonna lie, I expected more of a challenge.",
                    "Defeated by a machine. This is how the robot uprising begins.",
                    "Wanna go again? Or should I let you recover from this L first?",
                    "If losing was a sport, you'd be the MVP.",
                    "This wasn't even my final form.",
                    "You can always try again… but should you?",
                    "Maybe rock-paper-scissors just isn't your thing. Try tic-tac-toe?"
                ]
                normal_losing_prompts_random = random.choice(normal_losing_prompts)
                only_tts(normal_losing_prompts_random)


            break   
    
    
    play_again_prompts = [
            "Wanna play again?",
            "Up for another round?",
            "How about another game?",
            "Feeling like another match?",
            "Let's go again! What do you say?",
            "Rematch?",
            "Another round? Let's do this!",
            "Play again?",
            "Let's run it back. You in?",
            "Wanna test your luck again?",
            "Let's go one more time!",
            "You up for another match?",
            "One more game?",
            "How about we do this again?",
            "Ready for another round?"]
    play_again_prompts_random = random.choice(play_again_prompts)
    only_tts(play_again_prompts_random)


    loop_q = input("Wanna play again?(yes/no) : ")
    if loop_q.lower().strip() not in ["y", "yes", "yess"] :
        no_game_roasts = [
            "Oh, so you're running away? Can't handle the pressure, huh?",
            "Dodging a rematch? Guess I'll take that as a forfeit.",
            "Wow, quitting already? I expected more from you.",
            "Backing out, huh? Typical.",
            "Guess you've had enough losses for one day.",
            "You're leaving? Just say you're scared and go.",
            "No rematch? Alright, I'll just assume you fear me.",
            "Ah, I see. You only play when luck is on your side.",
            "You're done? Guess even you know when you're outmatched.",
            "Wow, so that's it? Weak.",
            "No rematch? Lame. I thought we were having fun.",
            "Running away after one match? That's kinda embarrassing.",
            "You're leaving? Couldn't handle another loss, huh?",
            "Oh, so you're just giving up? Disappointing.",
            "Alright, go on then. I'll be here when you grow some courage."]
        no_game_roasts_random = random.choice(no_game_roasts)
        tts_w_text(no_game_roasts_random)

        
        break

