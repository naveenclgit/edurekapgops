import sys
import csv
from tabulate import tabulate


def main():
    callvalidation()

    outname = []
    try:
        with open(sys.argv[1], "r") as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                fullname = row["name"].split(",")
                outname.append({"first": fullname[1].lstrip(), "last": fullname[0].lstrip(), "house": row["house"].lstrip()})

        with open(sys.argv[2], "w") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=["first","last","house"])
            writer.writeheader()
            for row in outname:
                writer.writerow({"first":row['first'] ,"last" : row['last'],"house":row['house']})

                #outname.append(row)
            #print(tabulate(outname, headers="keys", tablefmt="grid"))
            #ofile = open(sys.argv[2], "w")
            #ofile.write(tabulate(outname, headers="keys", tablefmt="grid"))
            #ofile.close()

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


def callvalidation():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()
