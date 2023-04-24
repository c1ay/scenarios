# This function takes in a list of tuples, where each tuple contains the number of seats and passengers for a bus.
def max_passengers(buses):
    # Create an empty list to store the maximum number of passengers that each bus can still take.
    max_passengers_list = []

    # Iterate over each tuple in the input list.
    for seats, passengers in buses:
        # Calculate the maximum number of passengers that can still fit on the bus.
        max_passengers = seats - passengers
        # Append this value to the list of maximum passenger counts.
        max_passengers_list.append(max_passengers)

    # Find the maximum value in the list of maximum passenger counts.
    max_passengers = max(max_passengers_list)
    # Return the maximum number of passengers that any bus can still take.
    return max_passengers
