# STUDENT GRADE SYSTEM
# Ask user for the number of students
# Store scores in a list
# Print: average score, highest score, lowest score
# For each score: 80+ - Grade A; 70+ - Grade B; 60+ - Grade C; Otherwise - Fail
# Print report cards
scores = []
while True:
    try:
        number = int(input("Enter total number of students: "))
        break
    except ValueError:
        print("Invalid input")
        continue

index = 1
names = []

# Collecting names and grades
while index <= number:
    try:
        name = input(f"Enter the name of student {index}: ")
        mark = int(input(f"Enter the score of student {index}: "))
        if 0 <= mark <= 100:
            names.append(name)
            scores.append(mark)
        else:
            print("Score must be between 0 and 100! Retry!")
            continue
    except ValueError:
        print("Wrong input format! Retry!")
        continue
    index += 1

# Assigning grades
a = b = c = f = 0
grades = []
for score in scores:
    if score >= 80:
        grades.append("A")
        a += 1
    elif score >= 70:
        grades.append("B")
        b += 1
    elif score >= 60:
        grades.append("C")
        c += 1
    else:
        grades.append("Fail")
        f += 1
print(f"Average score: {(sum(scores)/number):.2f}\nHighest score: {max(scores)}\nLowest score: {min(scores)}")

# Grade distribution
print(f"Grade A: {a} students\nGrade B: {b} students\nGrade C: {c} students\nFail: {f} students")

students = list(zip(names, scores, grades))

# Print report cards
for name, score, grade in students:
    print("_____Report card_____")
    print(f"Student's name: {name}\nScore: {score}\nGrade: {grade}\n")

# Students ranking
students.sort(key=lambda student: student[1], reverse=True)
print("_____Students ranking_____")
for rank, (name, score, grade) in enumerate(students, start=1):
    print(f"{rank}. {name} - Score: {score} - Grade: {grade}")