# with open("python/files_IO/practice/1/practice.txt","w") as f :
#     f.write("Hi evryone \n we are leaning File IO")
#     f.write("using Java \n I like programming in Java")
# f.close()

def replace_word(filename) :
    f=open(filename,"r")
    data=f.read()
    new_data=data.replace("Java","Python")
    print(new_data)
    return new_data

f=replace_word("python/files_IO/practice/1/practice.txt")

f1=open("python/files_IO/practice/1/practice.txt","w")
f1.write(f)
f1.close()

# search learning 
word="python"
def check_for_line(word):
    flag=True 
    line_no=1
    with open("python/files_IO/practice/1/practice.txt","r") as f :
        while flag :
            data=f.readline()
            if word in data :
                print("Line No : ",line_no)
                return 
            line_no+=1


    return -1 
check_for_line("learning")

 