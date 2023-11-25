import sys
import csv
from tabulate import tabulate


def main():
    callvalidation()

    menutab = []
    try:
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                menutab.append(row)
            print(tabulate(menutab, headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")


def callvalidation():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
