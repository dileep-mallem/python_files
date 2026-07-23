# true if Even or false 

n=5
def is_even(num):
    return  num%2==0 
print(is_even(n))

def find_max(a,b,c):
    if a>b :
        if a>c :
            return a 
        else :
            if c > b :
                return c 
    else :
        if b > c :
            return b 
    return 
print(find_max(9,6,4))

def factorial(n):
    c=1
    for i in range(1,n+1):
        c=c*i 
    return c 
print(factorial(n))

def count_vowels (word):
    v=0
    for char in word.lower() : 
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' :
            v+=1
    return v 
print(count_vowels("Dileep Kumar ROnaldo Virat ohli Kalyan Daemon "))

def reverse_string(word):
    n=len(word)
    rev=""
    for i in range(n-1,-1,-1):
        rev=rev+word[i]
    print("Reversed String : " ,rev)
reverse_string("Dileep")

