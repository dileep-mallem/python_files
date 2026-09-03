#Conditional Statements
age=int(input("Enter Your Age : "))

if age>=18:
    print("Your are Elgible for Voting")
else:
    print("Too Young to Vite")

grade=float(input("Enter Your Grade : "))
if grade>=100 or grade<0:
    print("Grade Should between o and 100")
elif grade>=90:
    print("A")
elif grade>=80 and grade<90:
    print("B")
elif grade>=70 and grade<80:
    print("C")
elif grade>=60 and grade<70:
    print("D")
else : #<=60
    print("F")

#Leap year
year=int(input("Entr Year : "))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")




    