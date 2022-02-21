
question_bank = ({'Question' : ' 3 + 4  , a. 7 , b. 8 , c. 6  , d. 9' ,'Answer' : 'a'} ,
                 {'Question' : '3 + 3  , a. 7 , b. 6 , c. 5  , d. 8' ,'Answer' : 'b' } ,
                 {'Question': '3 + 2  , a. 7 , b. 8 , c. 5  , d. 4', 'Answer': 'c'},
                 {'Question': '3 + 1  , a. 4 , b. 8 , c. 6  , d. 6', 'Answer': 'a'}
                 )
count1 = 0
count2 = 0

print("Welcome to the quiz program")
player1 = input("Enter name of player 1 : ")
player2 = input("Enter name of player 2 : ")


for i in range ( 0 , len(question_bank) , 2):
    print(f"{player1} , here is your question : ")
    print(question_bank[i]['Question'])
    ans = input("Enter your option :  ")
    if ( ans == question_bank[i]['Answer'] ):
        print("Correct Answer")
        count1 = count1 + 1
    else :
        print("Wrong Answer")

    print(f"{player2} , here is your question : ")
    print(question_bank[i+1]['Question'])
    ans = input("Enter your option :  ")
    if (ans == question_bank[i+1]['Answer']):
        print("Correct Answer")
        count2 =   count2 + 1
    else:
        print("Wrong Answer")

print("Score 1 " , count1)
print("Score 2 ", count2)