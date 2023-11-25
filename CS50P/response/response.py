import sys
from validator_collection import validators

def main():
    print(validate(input("What's your email address? ").strip()))


def validate(s):
    try:
        _ = validators.email(s)
        return "Valid"
    except:
        return "Invalid"


if __name__ == "__main__":
    main()