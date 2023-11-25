import sys

def main():
    callvalidation()
    tcdlines = 0
    try:
        file = open(sys.argv[1],"r")
        cdlines = file.readlines()
        #print(cdlines)
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)
    for line in cdlines:
        if line.lstrip().startswith('#') or line.isspace():
            tcdlines = tcdlines
        else:
            #print (line)
            tcdlines += 1

    print(tcdlines)


def callvalidation():
    if len(sys.argv) > 2:
        #print (f"{sys.argv}")
        print ("Too many command-line arguments")
        sys.exit(1)
    if len(sys.argv) < 2:
        #print (f"{sys.argv}")
        print ("Too few command-line arguments")
        sys.exit(1)
    if not sys.argv[1].endswith('.py'):
        #print (f"{sys.argv}")
        print ("Not a Python file")
        sys.exit(1)


if __name__ == "__main__":
    main()