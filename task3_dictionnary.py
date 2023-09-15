grade_weight_mapping = {"A": 4, "B": 3, "C": 2, "D": 1, "E": 0}

student_units = {
    "Math": {"grade": "A", "credits": 3},
    "Science": {"grade": "B", "credits": 4},
    "History": {"grade": "C", "credits": 3},
    "English": {"grade": "A", "credits": 2},
}

total_credits = sum(unit["credits"] for unit in student_units.values())
total_grade_points = sum(grade_weight_mapping[unit["grade"]] * unit["credits"] for unit in student_units.values())
GPA = total_grade_points / total_credits

student = {
    "name": "Bastien Rapaud",  
    "units": student_units,
    "total_credits": total_credits,
    "GPA": GPA
}

print(student)
