from typing import Dict, List, Tuple
import datetime


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
            current_month = datetime.datetime.now().month
            record_month = int(record[0][5:7])
            if current_month != record_month:
                continue

            # increment the total days counter
            total_days += 1

            # check the attendance status and increment the attendance days counter
            if record[1] == "P" or record[1] == "L":
                attendance_days += 1

        # calculate the attendance percentage for the student and add it to the dictionary
        attendance_percentage[student] = round(attendance_days / total_days * 100, 2)

    # return the dictionary with attendance percentages
    return attendance_percentage
