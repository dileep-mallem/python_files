word=input("Enter Word : ")
shift_no=int(input("Enter Shift Number : "))

encrypted_word=""

for char in word : 
    encrypted_word+=chr((ord(char)-97+shift_no)%26 +97 ) #Rounds Up 
print()
print(f"Given {word} , Its Encrypted word {encrypted_word}")
    
