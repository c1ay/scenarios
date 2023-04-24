# This function takes in a list of integers representing grade levels of students in a school.
def count_enrollment(enrollment_list):
    # Create an empty dictionary to store the enrollment counts for each grade level.
    enrollment_dict = {}

    # Iterate over each grade level in the input list.
    for grade_level in enrollment_list:
        # If the grade level is already in the dictionary, increment its enrollment count.
        if grade_level in enrollment_dict:
            enrollment_dict[grade_level] += 1
        # Otherwise, add the grade level to the dictionary with an enrollment count of 1.
        else:
            enrollment_dict[grade_level] = 1

    # Iterate over the range of grade levels 1-12 and add any missing grade levels to the dictionary
    # with an enrollment count of 0.
    for i in range(1, 13):
        if i not in enrollment_dict:
            enrollment_dict[i] = 0

    # Return the enrollment dictionary.
    return enrollment_dict
