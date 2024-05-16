student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}
student_grades = {}
for student in student_scores:
    if 91 <= student_scores[student] <= 100:
        student_grades[student] = "Outstanding"
    if 81 <= student_scores[student] <= 90:
        student_grades[student] = "Exceed Expectations"
    if 71 <= student_scores[student] <= 80:
        student_grades[student] = "Acceptable"
    if student_scores[student] <= 70:
        student_grades[student] = "Fail"
print(student_grades)
