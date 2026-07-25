# Text Files : .txt , .docx , .log et
# Binary Files : .mp4 , .mov , .png , .jpeg etc 

# Python can be used to perform operation on a file(read and Write)

# Open , read and close 
# we hve to open a file befire reading or writinf 

f=open("python/files_IO/demo.txt","r") # def mode : read
# x=f.read(5) 
data=f.read() # return full data(from starting cursor to end of file) in string form

line= f.readline() #  read one line at a time and ( get extra line cause of invisible \n )

print(data,type(data))
print(line)

f.close()

# modes : r , w (over write), x(create new file adn write) , a(append) , 
# b(binarymode),t(textmode) -> default , +(open a disk file for updating)(reading and writng)

# Writing to a file 

f=open("python/files_IO/demo.txt","w") # create file if not exisit
f.write("I want to learn file IP and Hashmaps today")
f.close()

f=open("python/files_IO/sample.txt","a")
f.write("Appending Data ")
f.close()

# r+ -> No Truncate
# w+ -> Truncatr (Overwrites)
# a+ -> append and writr 

f=open("python/files_IO/demo.txt","r+") # Overrites from cusor to end of sentence , remaing as it was   -> pointer at start
f.read()
f.write("\nDileep Kumar") 
f.close()

f=open("python/files_IO/demo.txt","w+") # Overrites everything from start  , pointer at start
f.read()
f.write("Dileep Kumar") 
f.close()

f=open("python/files_IO/demo.txt","a+") # appends from last  , pointer at end
f.read()
f.write("\nMAchine Learnig and DSA") 
f.close()

with open("python/files_IO/demo.txt","a+") as f : # as : alias 
    f.read()
    f.write("\nPYTHON and SQL") 
    f.close()

# Deleting a file (Using a os module) 
import os 
os.remove("python/files_IO/sample.txt") # Deleted 




