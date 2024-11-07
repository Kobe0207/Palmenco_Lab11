passed =+ 0
counter =+ 0
grade_list= []
num_students = int(input("Enter the number of students: "))

#Entering the total grades of the students
for i in range (num_students):
 grade = float(input("Enter the total grade of the students: "))
 if grade <= 39 and grade >= 101:
    print("Error! Invalid grade")
    break
 else:
     grade_list.append(grade)
 
 if grade >= 75:
    passed += 1
    counter += 1 
 else:
    counter += 1

 #Calculating the average

 if counter == (num_students):
    average = sum(grade_list) / (num_students)
    print("The average grade is: ", average)
    print("The number of students that passed are: ", passed)
    print("The number of students that failed are: ", counter - passed)
    
#Calculating the percentage of the students that passed 

percentage = (passed / len(grade_list)) * 100
passing_percentage = round(percentage, 2)

print("Final grade:" , grade_list)
print("Average grade: ", average)
print("The percentage of students that passed: ", passing_percentage, "%")
print("The percentage of students that failed: ", 100 - passing_percentage, "%")

    