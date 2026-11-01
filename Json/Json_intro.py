# JSon : javaScript Object Notation is independent lang , text foramt for exchanging structederd Data .# A
# API's , congfig Files , DB's , logs , ML pipelines Use it 
#  It grew popular in web APIs because it is compact and maps naturally to objects and arrays.
# XML remains useful for document-heavy and enterprise ecosystems; JSON did not eliminate XML.

# JSON (JavaScript Object Notation) is a text-based format used to store and exchange data. 
# Think of it as a universal language for data: it allows different programming languages (like Python, JavaScript, and Java) 
# to easily talk to one another because it uses a clean, human-readable structure of keys and values

# JSON IMp Funxtions : 
# json.dumps()	Python object → JSON string
# json.loads()	JSON string → Python object
# json.dump()	Python object → JSON file
# json.load()	JSON file → Python object
# json.JSONEncoder	Customize serialization
# json.JSONDecoder	Customize deserialization

import json 

user={
    "name" : "Dileep",
    "age" : 20 ,
    "is_student":True
}

json_data=json.dumps(user)
print("\njson.dumps()")
print(json_data)
print(type(json_data))

# {"name": "Dileep", "age": 20, "is_student": true}
# <class 'str'>
print("\n json.loads()")
user_data=json.loads(json_data)

print(user_data)
print(type(user_data))
print(user_data["name"],user_data["is_student"])

# {'name': 'Dileep', 'age': 20, 'is_student': True}
# <class 'dict'>
# Dileep True

# json.dump() # write JSON to a file 
user_data = {
    "name": "Dileep",
    "age": 20,
    "skills": ["Python", "SQL", "ML"]
}

with open("user_data.json","w",encoding="utf-8") as file : 
    json.dump(user_data,file,indent=4) # indent=4 It formats the JSON with four spaces of indentation, making it easier to read


print("\njson.load()") # read JSON from a file 
with open("user_data.json","r",encoding="utf-8") as file : 
    user_data=json.load(file)
print(user_data,type(user_data)) # {'name': 'Dileep', 'age': 20, 'skills': ['Python', 'SQL', 'ML']} <class 'dict'>

# Advanced Serializaion Ooptions 

# indent -> Controls Formating 

data={
    "name":"Dileep",
    "skills":["Python","DSA","ML"]
}
print(json.dumps(data,indent=8))
# {
#         "name": "Dileep",
#         "skills": [
#                 "Python",
#                 "DSA",
#                 "ML"
#         ]
# }

# sort_keys -> sorts dictionary keys alphabetically 

data={
    "zebra":10,
    "apple":20,
    "mango":30
}
print(json.dumps(data,sort_keys=True,indent=4))
# {
#     "apple": 20,
#     "mango": 30,
#     "zebra": 10
# }

# seprators -> controls seprators between JSON elements 
data={
    "name":"Dileep",
    "age":20
}

print(json.dumps(data,separators=(",",":"))) # {"name":"Dileep","age":20}
# This produces compact JSON by removing unnecessary spaces.

# ensure_ascii 
# By def , Python escape non-ASCII chars , ensrue_ascii=True (def)

data={
    "language":"తెలుగు"
}
print(json.dumps(data)) # {"language": "\u0c24\u0c46\u0c32\u0c41\u0c17\u0c41"}
print(json.dumps(data,ensure_ascii=False)) # {"language": "తెలుగు"}

# allow_nan 
# Python's JSON encoder allows NaN and infinity by default,allow_nan=True , even though these are not valid for standard JSON NUmbers . 

import math 
data={
    "score":math.nan
}
print(json.dumps(data)) # {"score": NaN} , not strict JSON
# print(json.dumps(data,allow_nan=False)) # ValueError: Out of range float values are not JSON compliant

# For APIs and interoperable data, strict JSON is generally preferable.