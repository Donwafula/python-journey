# Implementing functions in the new grading system

# INPUT FUNCTION
def get_student_data():
    while True:
        try:
            number = int(input("Enter total number of students: "))
            break
        except ValueError:
            print("Invalid input")
            continue

    names = []
    scores = []
    index = 1
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

    # print(f"{number}\n{names}\n{scores}")

# GRADE FUNCTION
def get_grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "c"
    else:
        return "Fail"

# STATISTICS FUNCTION
def calculate_stats(scores):
    a = b = c = f = 0
    for score in scores:
        if score >= 80:
            a += 1
        elif score >= 70:
            b += 1
        elif score >= 60:
            c += 1
        else:
            f += 1

    average = sum(scores)/len(scores)
    highest = max(scores)
    lowest = min(scores)
    
    print(average, highest, lowest)
    # Grade distribution
    print(f"Grade A: {a} students\nGrade B: {b} students\nGrade C: {c} students\nFail: {f} students")

# DISPLAY FUNCTION
def display_report(students):
    for name, score, grade in students:
        print("_____Report card_____")
        print(f"Student's name: {name}\nScore: {score}\nGrade: {grade}\n")  


