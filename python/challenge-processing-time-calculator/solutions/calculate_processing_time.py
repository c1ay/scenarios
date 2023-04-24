# define function named calculate_processing_time that takes in a parameter num_pages
def calculate_processing_time(num_pages):
    # if the number of pages is less than or equal to 10, return 1
    if num_pages <= 10:
        return 1
    # if the number of pages is less than or equal to 50, return 3
    elif num_pages <= 50:
        return 3
    # if the number of pages is less than or equal to 100, return 5
    elif num_pages <= 100:
        return 5
    # for any number of pages greater than 100, return 7
    else:
        return 7
