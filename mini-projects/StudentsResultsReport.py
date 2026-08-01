#Store student names as keys and a list of their marks (in different subjects) as values. Then process this data to generate a report.
# Write a function calculate_average(marks) that takes a list of marks and returns the average.
# Write a function assign_grade(average) that returns a grade (A, B, C, etc.) based on the average.
# For each student, print their name, average marks, and grade.
# Find and print the topper (student with the highest average).
# Bonus: Store the final result as a dictionary of tuples: {"Alice": (84.3, "A"), ...}


data = {
    "Dileep":[99,100,98,100],
    "Jon Snow":[89,90,99,76],
    "Tyler Durden":[99,78,45,32],
    "Peddi":[95,99,100,76]
}

def calucate_average(marks):
    avg,sum=0,0
    for i in range(0,len(marks)):
        sum+=marks[i]
    avg=sum/4
    return avg

def assign_grade(marks):
    sum=0
    for i in range(0,len(marks)):
        sum+=marks[i]
    per=(sum/4)  
    
    if per>90 and per <=100 :
        grade='A'
    if per>80 and per <=90 :
        grade='B'
    if per>65 and per <=80 :
        grade='C'
    if per>50 and per <=65 :
        grade='D'
    if per>=35 and per <=50 :
        grade='E'
    if per<35 :
        grade='F'
    return grade
def topper(avg):
    sum=0
    if avg >sum : 
        sum = avg 
    return sum 

for key,values in data.items():
    avg=calucate_average(values)
    print(f" Name : {key}   Average : {avg}")
print("------------")
for key,values in data.items():
    grade = assign_grade(values)
    print(f" Name : {key}   Grade : {grade}")
print("------------")
topper_avg=0
topper=""
for key,values in data.items():
    avg=calucate_average(values)
    if avg>topper_avg:
        topper_avg=avg
        topper=key
    

print(f" Topper : {topper} with average {topper_avg}   ")
print("------------")








