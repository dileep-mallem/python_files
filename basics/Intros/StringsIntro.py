#Strings = Series of Characters 

# name= input("Enter ur Full name : ")
# ph_no=input("Enter ur Phone Number : ")

#function

#result=len(name)
#help(str)


#Methods 

#result=name.find("e") -> First Occernences of char (-1 for if char is absent )
#result=name.rfind("e") -> Last Occernece of thar char ( r -> reverse )
#name.capitalize() -> Capitailze only first Letter of String
#name.upper() , name.lower()
#name=name.title() -> Capitaloze First Letter of all Worlds
#result=name.isdigit()# -> true if alll chars are digts , name.isalpha()
#result=ph_no.count("8") -> count no of char in that String , -1 if not
#ph_no=ph_no.replace("8","") -> replacing 8 with empty 

#Indexing = accessing elements of a sequence using [] (indexing Operation , [start , end , step]

credit_no="1234-5678-9812-3456"

print(credit_no[:7:-1]) #*

# join 
# oin() method in Python is a string method that takes an iterable (like a list, tuple, or set) of strings and merges them into one single string.

# the string u call join() on acts as the glue(or seprator) placed btwn each item 

# syntax : "glue".join(iterable_of_strings)

items=["a","b","c"]

x="-".join(items)
print(x) # a-b-c 

list_of_items=[["a","b","c"],["a","b","c"],["a","b","c"]]

# lets convert to list of strings 

list_of_strs=[" ".join(row) for row in list_of_items]
print(list_of_strs) # ['a b c', 'a b c', 'a b c']

lines = ["Row one data", "Row two data", "Row three data"]
multiline_string = "\n".join(lines)

print(multiline_string)
# Output:
# Row one data
# Row two data
# Row three data


# Non-String Elements

# join() only works if every single item inside the list is already a string. If you have an integer or a boolean in the list, Python will throw a TypeError.

mixed_list = ["User", 21, "Active"]
# result = "-".join(mixed_list) 
# TypeError: sequence item 1: expected str instance, int found 

