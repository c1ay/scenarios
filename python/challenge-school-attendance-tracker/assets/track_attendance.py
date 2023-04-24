from typing import Dict, List, Tuple


def track_attendance(attendance: Dict[str, List[Tuple[str, str]]]) -> Dict[str, float]:
    # initialize a dictionary to store the attendance percentage for each student
    attendance_percentage = {}

    # loop through each student
    for student, records in attendance.items():
        # initialize counters for total days and attendance days
        total_days = 0
        attendance_days = 0

        # loop through each attendance record for the student
        for record in records:
            # check if the attendance record is for the current month
            # you can use the datetime module to get the current month
            # and compare it with the month in the attendance record
            # if it's not for the current month, skip it
            pass

            # increment the total days counter
            pass

            # check the attendance status and increment the attendance days counter
            pass

        # calculate the attendance percentage for the student and add it to the dictionary
        pass

    # return the dictionary with attendance percentages
    pass
