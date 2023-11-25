def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s) < 2 or len(s) > 6 or s.isalnum() == False or s[:2].isalpha() == False:
        return False
    else:

        i = 0
        j = 0
        while i < len(s):
            if s[i].isdigit():
                if int(s[i]) == 0:
                    return False
                else:
                    break
            i += 1

        while j + 1 < len(s):
            if s[j].isdigit():
                if s[ j + 1 ].isalpha():
                    return False
            j += 1


        return True

if __name__ == "__main__":
    main()
