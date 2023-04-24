from typing import Dict

PRICING_RULES = {
    "Morning": 10,
    "Afternoon-Adult": 15,
    "Afternoon-Child": 10,
    "Evening-Adult": 20,
    "Evening-Child": 15,
}


def calculate_ticket_price(age: int, show_time: str) -> int:
    if age < 0:
        raise ValueError("Age cannot be negative")

    hour, minute = show_time.split(":")
    hour = int(hour)
    minute = int(minute)

    if hour < 0 or hour > 23 or minute < 0 or minute > 59:
        raise ValueError("Invalid show time")

    if hour < 12:
        return PRICING_RULES["Morning"]
    elif hour < 17:
        if age < 18:
            return PRICING_RULES["Afternoon-Child"]
        else:
            return PRICING_RULES["Afternoon-Adult"]
    else:
        if age < 18:
            return PRICING_RULES["Evening-Child"]
        else:
            return PRICING_RULES["Evening-Adult"]
