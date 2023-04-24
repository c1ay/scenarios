# Fire Station Alert System

The fire station is responsible for attending emergencies in a city. Emergencies are reported with a priority level and a location. To manage the emergencies, the station wants to develop an alert system that can add, remove, and prioritize emergencies.

## Example Usage

```python
# Create some Emergency instances
emergency1 = Emergency(3, '123 Main St')
emergency2 = Emergency(1, '456 Oak Ave')
emergency3 = Emergency(2, '789 Pine Rd')

# Create a FireStation instance and add the emergencies
fs = FireStation()
fs.add_emergency(emergency1)
fs.add_emergency(emergency2)
fs.add_emergency(emergency3)

# Prioritize the emergencies and remove the highest priority one
fire_station.prioritize_emergencies()
highest_priority = fire_station.emergencies.pop(0)

# Remove another emergency
fire_station.remove_emergency(emergency3)
```

## TODO

- Complete `fire_emergencies.py`

## Requirements

- Implement a class `Emergency` with attributes `priority` (int) and `location` (str).
- Implement a class `FireStation` with a list `emergencies`.
- Implement a method `add_emergency()` in `FireStation` class to add an emergency to the list.
- Implement a method `remove_emergency()` in `FireStation` class to remove an emergency from the list.
- Implement a method `prioritize_emergencies()` in `FireStation` class to sort the list of emergencies by priority.
- Implement the `__del__` method for the `Emergency` class.
