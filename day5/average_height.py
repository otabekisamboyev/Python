student_heights = input("Enter a list of student heights ").split()
for i in range(0, len(student_heights)):
    student_heights[i] = int(student_heights[i])

height = 0
number_of_student = 0
for n in student_heights:
    number_of_student += 1
    height += n
average_height = round(height / len(student_heights), 2)
print(f"Average height of {number_of_student} students is {average_height}")
