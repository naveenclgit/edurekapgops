def main():
    gas = input("Fraction: ")
    print (gauge(convert(gas)))

def convert(fraction):
    while True:
        try:
            C,T = fraction.split("/")

            c = int(C)
            t = int(T)

            pa = c / t

            if pa <= 1:
                pc = int(pa * 100)
                return pc
            else:
                fraction = input("Fraction: ")
                pass

        except (ValueError, ZeroDivisionError):
            raise

def gauge(percentage):
    pa = int(percentage)
    if pa <= 1:
        return "E"
    elif pa >= 99:
        return "F"
    else:
        return str(pa) + "%"


if __name__ == "__main__":
    main()
