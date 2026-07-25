with open("python/files_IO/practice/2/numbers.txt","r") as f :
    data=f.read()
    l=data.split(",")
    c=0
    for i in l :
        if int(i)%2 == 0 :
            c+=1
    print("Even NOumbers : ",c)  