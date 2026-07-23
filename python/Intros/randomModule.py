import random

# print(help(random))


#number = random.randint(low,high)
#number = random.random() -> foalting point number between 0 and 1

a= random.randint(1,101)
choices=["Rock","Paper","Scissor"]
n=random.choice(choices)
print(a,n)

