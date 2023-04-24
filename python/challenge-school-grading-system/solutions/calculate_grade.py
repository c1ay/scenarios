# This function takes in a dictionary containing information about a student's academic performance.
def calculate_grade(student_info):
    # Extract the student's assignment scores, test scores, and attendance percentage from the input dictionary.
    assignments = student_info["assignments"]
    tests = student_info["tests"]
    attendance = student_info["attendance"]

    # Calculate the highest assignment score and the highest test score.
    max_assignment = max(assignments)
    max_test = max(tests)

    # Calculate the student's final grade by weighting the highest assignment and test scores
    # and the attendance percentage and rounding the result to the nearest whole number.
    final_grade = round((max_assignment * 0.5) + (max_test * 0.4) + (attendance * 0.1))

    # Return the final grade.
    return final_grade
