import random, time

#Variables
keepPlaying = True
plrName = input("What is your name? ")
print("Hello, "+plrName+"! Are you ready to lose? Let's play!")
time.sleep(1)

#RPS Function
def output(crps, prps, kp):
    if (crps==prps):
        print("Tie! Try again!\n")
    elif ((crps=="rock" and prps=="scissors") or (crps=="paper" and prps=="rock") or (crps=="scissors" and prps=="paper")):
        print("Hah! You lose!\n")
            
    elif ((crps=="rock" and prps=="paper") or (crps=="paper" and prps=="scissors") or (crps=="scissors" and prps=="rock")):
        print("Aw, how did you win? I'm usually really good at this game! Are you cheating?!\n")

#While Loop                
while (keepPlaying!=False):
    plrRPS = input("Rock, Paper, Scissors... [Type 'Rock', 'Paper', or 'Scissors' to Choose] ")
    if(plrRPS.lower()=="rock" or plrRPS.lower()=="paper" or plrRPS.lower()=="scissors"):
        comRPS = " "
        comRand = random.randint(1,3)
        if (comRand==1):
            comRPS = "rock"
            print("Computer: Rock")
            output(plrRPS.lower(), comRPS, keepPlaying)
        elif (comRand==2):
            comRPS = "paper"
            print("Computer: Paper")
            output(plrRPS.lower(), comRPS, keepPlaying)
        elif (comRand==3):
            print("Computer: Scissors")
            comRPS = "scissors"
            output(plrRPS.lower(), comRPS, keepPlaying)
    else:
        tryAgain = input("Hm, it doesn't seem like that worked. You can either try again or quit. [Type 'Again' to try again or 'Quit' to quit the game]\n")
        if (tryAgain.lower()=="quit"):
            keepPlaying = False
        else:
            print(" ")
    
print("Thank you for playing! Check out more of my projects at https://github.com/Caleb-Kronstad")
