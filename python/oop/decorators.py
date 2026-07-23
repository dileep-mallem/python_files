# @decorators  -> We use on any method in the class to se the method as property
class student :
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem 
        self.math=math 
        #self.percentage=str((self.phy + self.chem + self.math) / 3)+"%"
        
    # def calcPercentage(self):
    #     self.percentage=str((self.phy + self.chem + self.math) / 3)+"%"
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3)+"%"

s1 = student(98,97,56) 
# print(s1.percentage)

# s1.phy=86 
# print(s1.percentage) #Percentage doesnt chane 
# s1.calcPercentage()
# print(s1.percentage) #It changes (One method)

s1.phy=86 
print(s1.percentage) #It Changes

# @setter and @getter 