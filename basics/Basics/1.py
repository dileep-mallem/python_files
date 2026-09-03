print("Hello World !")

#Variables : A NAmed Container
name="Dileep Kumar"
city="Kadapa"
age=19
gpa=9.85
is_Student=True

print(f"Name : {name} . City : {city} ")
print("Python","is","Fun",sep=",")

a,b,c=5,3,10
print(f"Sum : {a+b}") #8

#Type Check
print("Name Type :",type(name),"Age Type :",type(age),sep=",") #<class 'str'>

#Swap
print(f"a : {a} b : {b}")
a=a+b
b=a-b
a=a-b
print(f"After Swapping : a : {a} b : {b}")

score=0
score+=10
score*=2
print(score)


#Type Casting
num="50"
print(f"Num +25 : {int(num)+25}")
f=3.99
print(int(f))
year=2025
print(f"Year:{str(year)}")
print("Year:"+str(year))

 #Boolean Casting
print(bool(0),bool(1))
print(bool("")) #false







