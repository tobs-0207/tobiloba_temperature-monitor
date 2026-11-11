# Temperature Monitor and Alarm Checker
# Reads 5 machine temperatures, shows highest/lowest/average,
# warns if any reading is above the safe limit,
# and (my own twist) warns about sudden temperature jumps.

SAFE_LIMIT = 80.0       # safe temperature limit in degrees Celsius
MAX_JUMP = 10.0         # biggest normal rise between two readings (twist)
NUMBER_OF_READINGS = 5  # how many readings we collect


def get_reading(number):
    """Ask for one temperature and keep asking until it is a valid number."""
    while True:
        text = input(f"Enter temperature reading {number} (°C): ")
        try:
            return float(text)  # convert the typed text to a decimal number
        except ValueError:
            # The user typed letters or nothing, so explain and try again
            print("Invalid input. Please type a number, for example 72.5")


def check_limit(readings):
    """Warn about every reading that is above the safe limit."""
    danger_found = False
    for index, value in enumerate(readings, start=1):
        if value > SAFE_LIMIT:
            print(f"WARNING: Reading {index} ({value:.1f}°C) is above the safe limit of {SAFE_LIMIT}°C!")
            danger_found = True
    if not danger_found:
        print(f"All readings are within the safe limit of {SAFE_LIMIT}°C.")


def check_rapid_rise(readings):
    """MY TWIST: warn if the temperature jumps up too fast between two readings."""
    jump_found = False
    for i in range(1, len(readings)):
        change = readings[i] - readings[i - 1]  # difference from the previous reading
        if change > MAX_JUMP:
            print(f"RAPID RISE: +{change:.1f}°C between reading {i} and reading {i + 1}. "
                  "Possible overheating, please inspect the machine!")
            jump_found = True
    if not jump_found:
        print(f"No sudden temperature jumps (limit is {MAX_JUMP}°C between readings).")


def main():
    print("=== Temperature Monitor and Alarm Checker ===")
    readings = []  # the list that stores all readings

    # Loop to collect the 5 readings
    for number in range(1, NUMBER_OF_READINGS + 1):
        readings.append(get_reading(number))

    # Statistics
    highest = max(readings)
    lowest = min(readings)
    average = sum(readings) / len(readings)

    print("\n--- Results ---")
    print(f"Readings: {readings}")
    print(f"Highest: {highest:.1f}°C")
    print(f"Lowest:  {lowest:.1f}°C")
    print(f"Average: {average:.1f}°C")

    print("\n--- Alarm Checks ---")
    check_limit(readings)
    check_rapid_rise(readings)

    # Overall status using if/elif/else
    print("\n--- Overall Status ---")
    if highest > SAFE_LIMIT:
        print("DANGER: Machine exceeded the safe temperature.")
    elif highest > SAFE_LIMIT - 10:
        print("CAUTION: Machine is close to the safe limit.")
    else:
        print("NORMAL: Machine temperature is fine.")


main()
