# CREATING A GAME OF ROCK, PAPER AND SCISSOR
import random
opt=["ROCK","PAPER","SCISSOR"]
print("RULE OF THE GAME IF YOUR CHOICE AND COMPUTER CHOICE IS SAME IN THAT CASE THE MATCH IS TIE AND BOTH OF YOU GOT 1 SCORE")
print("OTHERWISE IF YOU WIN YOU GOT 1 POINT AND COMPUTER GOT 0 POINT AND SAME HAPPEND IF YOU LOOSE")
while True:
    print("ROCK, PAPER AND SCISSOR ")
    yous,comps=0,0
    for i in range(1,6):
        print("\nRound",i,"Start")
        print("Choose Betweeen ROCK, PAPER AND SCISSOR ")
        user=input("ENTER YOUR CHOICE = ")
        comp=random.choice(opt)
        print(f"Your Choice = {user}, Computer Choice = {comp}")
        if user==comp:
            yous+=1
            comps+=1
            print("THIS MATCH IS TIE YOU BOTH GOT +1 POINT ")
        elif user=="ROCK":
            if comp=="PAPER":
                comps+=1
                print("PAPER COVERS THE ROCK SO - COMPUTER WIN ")
            else:
                yous+=1
                print("ROCK SMASH THE SCISSOR SO - YOU WIN ")
        elif user=="PAPER":
            if comp=="ROCK":
                yous+=1
                print("PAPER COVERS THE ROCK SO - YOU WIN ")
            else:
                comps+=1
                print("SCISSOR CUTS THE PAPER SO - COMPUTER WIN ")
        elif user=="SCISSOR":
            if comp=="PAPER":
                yous+=1
                print("SCISSOR CUTS THE PAPER SO- YOU WIN ")
            else:
                comps+=1
                print("ROCK SMASH THE SCISSOR SO - COMPUTER WIN ")
        else:
            print("....INVALID CHOICE....")
    if yous>comps:
        print("\nYOU WIN THE MATCH AGAINST THE COMPUTER")
        print(F"YOUR TOTAL SCORE = {yous}, COMPUTER TOTAL SCORE = {comps} ")
    elif comps>yous:
        print("\nCOMPUTER WIN THE MATCH ")
        print(F"YOUR TOTAL SCORE = {yous}, COMPUTER TOTAL SCORE = {comps} ")
    else:
        print("\nMATCH DRAWS ")
        print(F"YOUR TOTAL SCORE = {yous}, COMPUTER TOTAL SCORE = {comps} ")
    user_choice_again=input("\nWANT TO PLAY AGAIN?? TYPE (YES/NO) = ")
    if  user_choice_again=="YES"or user_choice_again=="Yes" or user_choice_again=="yes":
        continue
    else:
        break


