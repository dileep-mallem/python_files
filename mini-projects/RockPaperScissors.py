# Rock -> Paper (win) Scissor(draw)
#paper -> scissor(win) 
#scissor -> paper(lose) Rock(draw)

#draw -> two same or rock and Scissor
#win -> paper if rock , scissor if paper 
import random , time 

choices = ["Rock" , "Paper" , "Scissor"]

flag,my_score,your_score=True ,0,0

print("Total Score for WIn : 3")

while flag==True  :
    for i in range(1,4):
        time.sleep(0.5)
        print(i)
    
    y = input("Enter Your Choice : ").capitalize()
    x=random.choice(choices) 
    print("My Choice : ",x)
    

    if x==y :
        print("Draw")
    elif x=="Rock":
        if y=="Paper" :
            print("You Won !!")
            your_score+=1
        if y=="Scissor":
            print("I won !!")
            my_score+=1 
    elif x=="Paper" :
        if y=="Rock" :
            print("You Lose !!")
            my_score+=1
        if y=="Scissor":
            print("You Won !!")
            your_score+=1
    elif x=="Scissor":
        if y=="Paper":
            print("You Lose!!")
            my_score+=1
        if y=="Rock":
            print("You WIn !!")
            your_score+=1
    else :
        print("Choose Correct Option (Rock/Paper/Scissor)")
    print(f"My Score : {my_score}    Your Score : {your_score}")
    print("------------")
    if my_score==3 or your_score==3:
        print("GAME OVER ")
        if my_score>your_score:
            print("I WON!!!!!!!!!")
        elif my_score<your_score :
            print("YOU WIN!!!!!!!!!")
        break
    continue_falg=input("You want to contine(y) or Exit(any other char) : ").lower()
    if continue_falg!='y' :
        print("----GAME COVER----")
        if my_score>your_score:
            print("I WON!!!!!!!!!")
        elif my_score<your_score :
            print("YOU WIN!!!!!!!!!")
        else :
            print("GAME DRAW ")
        flag=False 
print()

            


