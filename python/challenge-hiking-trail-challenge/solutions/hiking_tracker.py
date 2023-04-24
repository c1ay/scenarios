def hiking_tracker(hikers):
    # Initialize an empty dictionary to store hiker's location
    hiker_locations = {}

    # Loop through each hiker and add their location to the dictionary
    for hiker in hikers:
        name, location = hiker
        # Add hiker's name and location to the dictionary
        hiker_locations[name] = location

    # Return the dictionary
    return hiker_locations
