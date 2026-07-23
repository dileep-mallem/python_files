#Count of frequency if  each word in a Sentence using Dictionaries
sen="if the old persons became new when new persons came then old ones should behave as new "
list=sen.split()
print(list)
dic={}
for i in range(0,len(list)):
    count=0
    for j in range(0,len(list)):
        if list[i]==list[j] :
            count+=1
    dic.setdefault(list[i],count)
print(dic)

#key with maximum value in dictionary
c,k=0,""
for key,value in dic.items():
    if dic.get(key)>c:
        c=dic.get(key)
        k=key
print(f"{k} : {c}")