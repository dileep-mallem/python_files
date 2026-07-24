# to build Stack class , We can use Lists with Fixed capacity 

class Stack :

    def __init__(self,capacity : int) :
        self.capacity=capacity
        self.stack=[]

    def push(self,x : int):
        if len(self.stack)>=self.capacity :
            print("Stack OverFlow !!")
        else :
            self.stack.append(x) 
    def pop(self):
        if len(self.stack)==0:
            print("Stack UnderFlow !!")
        else :
            print(f"Popped : {self.stack.pop()}") 
    def display(self):
        if len(self.stack)==0:
            print("Stack is Empty !!")
        else :
            print(f"Stack : {self.stack}")
    def topElement(self):
        if len(self.stack)==0:
            print("Stack is Empty !!")
        else :
            print(f"Top Element : {self.stack[-1]}") 
        
n=int(input("Enter Sixe of Stack(int) : "))
s=Stack(n)

flag=True

while flag==True : 
    print("-- 1.Push 2.Pop 3.Deisplay 4.Top Element 5.Exit --")

    choice = int(input("Enter Choice (1-5) : "))

    match choice :
        case 1 :
            x=int(input("Enter Element You want to Push: "))
            s.push(x)
             
        case 2 :
            s.pop()
           
        case 3 :
            s.display()
         
        case 4 :
            s.topElement()
            
        case 5 :
            flag=False 
        case _ :
            print("Enter Coreect Choice !!")
print("-------------")

            




