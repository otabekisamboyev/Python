student_scores = input("Enter a list of student scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])


highest_score = student_scores[0]
for score in range(0, len(student_scores)):
    if student_scores[score] > highest_score:
        highest_score = student_scores[score]

print(f"The highest score in the class {highest_score}")
