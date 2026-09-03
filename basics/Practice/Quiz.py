#Quetions Quiz

quetions=("What is Nolan's Upcoming Movie ??" ,
           "MArvels Upcoming Movie", 
           "No of Virats Centuries", 
           "Roanaldo's International Goals",
            "Prsent Deputy CM of Ap " )
options=(("A.Batman 2 " , "B.Super Man ","C.Dark Knight rule ","D.The Odessey"),
         ("A.Spiderman BND " , "B.Avengers DoomsDay ","C.Thor Strongest Avenger ","D.Loki-God of Multiverse "),
         ("A.81 " , "B.83 ","C.84 ","D.86 "),
         ("A.975+ " , "B.990+ ","C.980+ ","D.985+ "),
         ("A.Pawan Kalyan" , "B.CBN ","C.Ram Charan ","D.Dileep "))
score=0
answers=["D","A","D","A","A"]
quetions_num=0
guess=[]

for question in quetions:
    print("---------------")
    print(question)
    for option in options[quetions_num]:
        print(option)
    ans=input("Enter Correct Answer : ").upper()
    guess.append(ans)
    if guess[quetions_num]==answers[quetions_num]:
        score+=1
        print(f"CORRECT !! Your Score is {score}")
    else :
        print("INCORRECT")
        print(f"Correct Option is {answers[quetions_num]}")
        
    quetions_num+=1
print()

