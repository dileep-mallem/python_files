#default args = A def value for certain parameters default is used when that argument is Omiited 
#               make ut functions more flecxible , reduces # of Args 


def net_price(list_price , discount =0 , tax=0.05):
    return list_price * (1 - discount) * (1 + tax) 

print(net_price(500))
print(net_price(500,0.1,0)) # if we give args Manually , they take it even though defalut values are There

import time

def count( end , start =0): #Non - default args should follow def args
    for x in range(start , end + 1) :
        print(x)
        time.sleep(0.4) # 1 = 1 sec
    print("DONE !")
count(7)
count(5,1)

