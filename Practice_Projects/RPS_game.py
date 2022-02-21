import random

computer_selection = random.choice(['rock' ,'paper' ,'scissor'])

computer_score = 0
your_score = 0

print("Welcome to the game")
selection = "y"

while selection == "y":
    computer_selection = random.choice(['rock', 'paper', 'scissor'])
    print("Computer Selected it's choice")
    your_selection = input("Make your selection ( a. Rock , b. paper , c. scissor ) : " )
    print(computer_selection)
    if (your_selection == "a" ):
        if(computer_selection == 'paper'):
            print(f"You selected Rock and computer selected {computer_selection}....Computer won")
            computer_score +=1
        elif(computer_selection == 'scissor'):
            print(f"You selected Rock and computer selected {computer_selection}....You won")
            your_score += 1
        else:
            print("Tie")
    elif (your_selection == "b" ):
        if(computer_selection == 'scissor'):
            print(f"You selected Paper and computer selected {computer_selection}....Computer won")
            computer_score +=1
        elif(computer_selection == 'rock'):
            print(f"You selected Paper and computer selected {computer_selection}....You won")
            your_score += 1
        else:
            print("Tie")
    elif (your_selection == "c" ):
        if(computer_selection == 'rock'):
            print(f"You selected Scissor and computer selected {computer_selection}....Computer won")
            computer_score +=1
        elif(computer_selection == 'paper'):
            print(f"You selected Scissor and computer selected {computer_selection}....You won")
            your_score += 1
        else:
            print("Tie")
    else:
        print("Wrong selection")

    selection = input( "Press Y to continue  : ").lower()

print ( "Your score is : " ,your_score )
print ( "Computer score is : " ,computer_score )
if(your_score == computer_score):
    print("Its a tie")
else:
    won = "You" if your_score > computer_score else "Computer"
    print(f"{won} won this game")

print("Quiting game")