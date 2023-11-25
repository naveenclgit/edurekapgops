import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    umc = re.findall(r"\b\W*um\b\W*",s,re.IGNORECASE)
    #print (umc)
    return len(umc)


if __name__ == "__main__":
    main()