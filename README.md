# Temperature Monitor and Alarm Checker

## What it does
This program reads 5 temperature readings from a machine and stores them in a list. It prints the highest, lowest and average temperature, and warns if any reading is above the safe limit of 80°C. It also gives an overall status of NORMAL, CAUTION or DANGER.

## How to run it
Install Python 3, then run: python temperature_monitor.py

## Sample output
```
=== Temperature Monitor and Alarm Checker ===
Enter temperature reading 1 (°C): abc
Invalid input. Please type a number, for example 72.5
Enter temperature reading 1 (°C): 60
Enter temperature reading 2 (°C): 65
Enter temperature reading 3 (°C): 80
Enter temperature reading 4 (°C): 92
Enter temperature reading 5 (°C): 70

--- Results ---
Readings: [60.0, 65.0, 80.0, 92.0, 70.0]
Highest: 92.0°C
Lowest:  60.0°C
Average: 73.4°C

--- Alarm Checks ---
WARNING: Reading 4 (92.0°C) is above the safe limit of 80.0°C!
RAPID RISE: +15.0°C between reading 2 and reading 3. Possible overheating, please inspect the machine!
RAPID RISE: +12.0°C between reading 3 and reading 4. Possible overheating, please inspect the machine!

--- Overall Status ---
DANGER: Machine exceeded the safe temperature.
```

## My own twist
A rapid-rise warning. The program compares each reading with the one before it and warns if the temperature jumps by more than 10°C. A machine can be below the safe limit and still be heating up dangerously fast, so this gives an early warning before the limit is reached.

## What I learned
- How to check user input with `try` and `except` so the program does not crash when someone types a letter instead of a number.
- How to use a list and loops to compare readings with each other, not only to find the highest and lowest.

## Author
Olaoluwa Tobiloba Elijah, ND1 Mechatronics Engineering, YabaTech.
