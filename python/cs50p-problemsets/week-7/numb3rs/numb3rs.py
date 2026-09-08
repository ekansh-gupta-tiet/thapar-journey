import re
import sys

def main():
    print(validate(input("IPv4 Adress: ")))

def validate(ip):
    pattern = r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$"
    match = re.search(pattern, ip)

    if not match:
        return False

    for group in match.groups():
        if not (0 <= int(group) <= 255):
            return False

    return True

if __name__ == "__main__":
    main()
