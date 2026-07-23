# dict = stires data as key : value pairs
#keys must be unique and immutable
#Dict's are Ordered(Python  3.7+) and mutable

student = {
    "name" : "Dileep",
    "age" : 20,
    "grade" : "OG",
    "score":98.5
}

#Accesing Vlaue

print(student["name"])
print(student.get("age")) # wont crash if key is missing
print(student.get("phone","N/A")) #"N/A" (default value)


#Adding / Updating
student["email"] = "mailtodileepmallem@gmail.com"
student["age"]=21
student.setdefault("job",0)

#Deleting
del student["score"] #delete a key
grade = student.pop("grade") # rempoves and returns value
# .clear() -> clears dict

#keys , valus , itens
print(student.keys(),student.values(),student.items()) #dict_keys(['name', 'age', 'email']) dict_values(['Dileep', 21, 'mailtodileepmallem@gmail.com']) dict_items([('name', 'Dileep'), ('age', 21), ('email', 'mailtodileepmallem@gmail.com')])

#looping in dic's
for key , value in student.items():
    print(f" {key} : {value}")
print()

#Nested Dic's
class_data={
    "Alice" : { "math" : 90 , "Science" :100},
    "Bob" : { "math" : 96 , "Science" :98}
}
print(class_data["Alice"]["math"])

#Dict comprehension
squares = { x : x**2 for x in range(1,6)}
print(squares)


