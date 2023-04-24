class Emergency:
    def __init__(self, priority, location):
        self.priority = priority  # Initialize the priority of the emergency
        self.location = location  # Initialize the location of the emergency

    def __del__(self):
        # Print a message when emergency object is deleted
        print(f"Emergency at {self.location} is being deleted.")


class FireStation:
    def __init__(self):
        self.emergencies = []  # Initialize an empty list of emergencies

    def add_emergency(self, emergency):
        # Add the emergency object to the list of emergencies
        self.emergencies.append(emergency)

    def remove_emergency(self, emergency):
        # Remove the emergency object from the list of emergencies
        self.emergencies.remove(emergency)
        del emergency  # Delete the emergency object

    def prioritize_emergencies(self):
        # Sort the list of emergencies by priority, lowest to highest
        self.emergencies.sort(key=lambda x: x.priority)
