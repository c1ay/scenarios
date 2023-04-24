# import the random module to generate random numbers
import random

# define a function to generate a list of unique postal codes


def generate_postal_codes(n):
    postal_codes = []  # initialize an empty list to store generated postal codes

    for i in range(n):  # loop through n times to generate n postal codes
        while True:
            # loop indefinitely until a new and unique postal code is generated

            # generate a new postal code between 10001 and 99999
            postal_code = str(random.randint(10001, 99999))

            # check if the postal code is already in the list of generated postal codes
            if postal_code not in postal_codes:
                # add newly generated unique postal code to the list of postal codes
                postal_codes.append(postal_code)
                break  # exit the loop to generate next postal code

    return postal_codes  # return the list of generated postal codes
