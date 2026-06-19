#name of the student
name = input("Enter your name: ")

#marks in each subject
first_language = int(input("first language marks: "))
second_language = int(input("second language marks: "))
third_language = int(input("third language marks: "))
maths = int(input("maths marks: "))
science = int(input("science marks: "))
social = int(input("social marks: "))

#total, average, percentage
Total = first_language + second_language + third_language + maths + science + social

Average = round(Total/6,2)

Percentage = round((Total/600)*100,2)

print("Student: ", name)
print("Total marks: ", Total)
print("Average: ", Average)
print("Percentage: ", Percentage)

#pass or fail
if Percentage >= 35:
    print("PASS!")
else:
    print("FAIL!")
