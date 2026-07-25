word=input("Enter Word : ")

#1.Print 1st,last andmiddle Char 
print(f"First : {word[0]} Last : {word[-1]} Middle : {word[(len(word))//2]}")

#Palindrome Check 
rev=word[::-1]
label="A Palindrome" if rev==word else "Not a Palindrome"
print(label)

#Slicing Practise
s="ABCDEFGHIJ"
print(f"First 3 {s[:3]} Last 3 {s[-3]} Revered String : {s[::-1]} 3-7:{s[3:8]} ")

#Extract Domain from Email
email="r230366@rgukurkv.ac.in"
n=email.find("@")
print(f"Domain of Email : {email[n+1:]}")