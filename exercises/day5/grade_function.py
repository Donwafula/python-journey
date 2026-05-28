# grading system

def get_grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score <= 60:
        return "C"
    else:
        return "Fail"

print(get_grade(80))
