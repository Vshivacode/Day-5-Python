# Find the avg of students_height
students_height = input("enter the number find average: ").split(",")
for num in range(0, len(students_height)):
    students_height[num] = int(students_height[num])
result = 0
for item in students_height:
    result += item
print(f"total: {result}")
no_of_students = len(students_height)
print(f"no_of_students: {no_of_students}")
avg = round(result/no_of_students)
print(f"average of students heights is: {avg}")


#Output:
enter the number find average: 23,48,10,89,39
total: 209
no_of_students: 5
average of students heights is: 42
