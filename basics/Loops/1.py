#INput
n=int(input("Enter Number : "))

#Print 1 to 10
for i in range(1,n+1):
    print(i,end=" ") #1 2 3 4 5
print() #New Line

#Sum of n 
sum=0
for i in range(1,n+1):
    sum+=i
print(f"Sum of First {n} Numbers is {sum}")
print()

#Multiplvation Table
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")
print()

#CountDown Timer
count=10
while count>=1:
    print(count,end=" ")
    count-=1
print()
print("Blast Off")
print()

#Skip Multiples of Three
for i in range(1,21):
    if(i%3==0):
        continue
    else:
        print(i,end=" ")
print()
print()
#Factorial
fact=1
for i in range(1,n+1):
    fact*=i 
print(f"Factorial of {n} is {fact}")

#Right Angled Triangle
print()
for i in range(1,n+1):
    for i in range(1,i+1):
        print("*",end=" ")
    print()
print()

#Guess the Correct Num
num=7
while True:
    n1=int(input("Enter Number : "))
    if(n1==num):
        print("Correct!!")
        break 
    elif n1>num:
        print("Too High")
    elif n1<num:
        print("Too Low")
print()

#Fizz Buzz
for i in range(1,31):
    if i%3==0 and i%5==0 :
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
print()