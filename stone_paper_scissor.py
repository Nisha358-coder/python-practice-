import random 

com = random . randint(1,3)
human_score = 0
computer_score = 0

while True:
    print(f"your current score is {human_score} , computer current score is {computer_score} \n")
    user = int(input("1 for stone , 2 for paper , 3 for scissors choose - "))

    if user == 1 and com == 3:
        human_score += 1
        print("you won this round \n")

    elif user == 2 and com == 1 :
        human_score += 1
        print("you won this round \n")

    elif user == 3 and com == 2:
        human_score += 1
        print("you won the round \n ")

    elif user == com:
        print("it's was a draw")

    else:
        computer_score += 1
        print("computer won this round")
    
    if computer_score == 5:
        print("computer won this game")
        break
    elif human_score == 5:
        print("you won this game")
    break 