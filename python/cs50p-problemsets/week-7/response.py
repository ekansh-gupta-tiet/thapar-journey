import sys
from validator_collection import validators, errors


def main():
    print(validate(input("What's your email address? ")))


def validate(s):
    try:
        if validators.email(s):
            return "Valid"
    except (errors.EmptyValueError, errors.InvalidEmailError):
        return "Invalid"


if __name__ == "__main__":
    main()
