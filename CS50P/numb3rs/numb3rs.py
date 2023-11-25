import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    iprange = re.match(r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$",ip)
    if iprange:
        return True
    return False


if __name__ == "__main__":
    main()