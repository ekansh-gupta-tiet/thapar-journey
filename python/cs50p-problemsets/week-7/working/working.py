import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r"^([1-9]|1[0-2])(?::([0-5][0-9]))?\s+(AM|PM)\s+to\s+([1-9]|1[0-2])(?::([0-5][0-9]))?\s+(AM|PM)$"
    match = re.search(pattern, s)

    if not match:
        raise ValueError("Invalid Format")

    h1, m1, period1, h2, m2, period2 = match.groups()

    time1 = format_24hr(h1, m1, period1)
    time2 = format_24hr(h2, m2, period2)

    return f"{time1} to {time2}"

def format_24hr(hour_str, minute_str, period):
    hour = int(hour_str)
    minute = int(minute_str) if minute_str else 0

    if period == "AM":
        if hour == 12:
            hour = 0
    elif period == "PM":
        if hour != 12:
            hour += 12

    return f"{hour:02d}:{minute:02d}"


if __name__ == "__main__":
    main()
