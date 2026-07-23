# Operator Over Loading 
# When the Same opearator is allowed to have differnt meaning according to the context 

print(1+2)
print("Dileep" +" Kumar") # concatenate 
print([1,2,3]+[4,5,6]) # merge 

class Complex :
    def __init__(self,real,img):
        self.real=real 
        self.img=img 

    def showNumber(self):
        print(self.real," + ",self.img,"i")

    def __add__(self,n2):
        newReal=self.real+n2.real 
        newImg=self.img+n2.img 
        return Complex(newReal,newImg)

n1=Complex(2,3)
n1.showNumber()
n2=Complex(5,7)
n2.showNumber()
# print(n1.add(n2))


#Opearators and Dunder Functions 
# a + b # addition a.__add__(b) ,__sub__,__mul__,__mod__
# a/b #division a.__truediv__(b)

# n 3= n1 + n2 -> Error 

n3=n1+n2 

n3.showNumber() # It gives 