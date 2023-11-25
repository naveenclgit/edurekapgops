import sys
import re
import inflect
from datetime import date

p = inflect.engine()

def main():
    dob = input("Date of Birth: ").strip()
    convdob = dob_validate(dob)
    #print(convdob)
    #words = p.number_to_words(convdob['year'], andword="")
    #words = words + " " + p.number_to_words(convdob['month'], andword="")
    #words = words + " " + p.number_to_words(convdob['date'], andword="")
    #print (f"{words}")
    textage = convert2min(convdob)
    print(f"{textage}")


def dob_validate(dob):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$",dob):
        yy,mm,dd = dob.split("-")
        return {"year":yy,"month":mm,"date":dd}
    else:
        sys.exit("Invalid date")

def convert2min(validdob):
    age = (date.today() - date(int(validdob['year']),int(validdob['month']),int(validdob['date'])))
    agemin = age.days * 24 * 60
    return (f"{p.number_to_words(agemin, andword='').capitalize()} minutes")


if __name__ == "__main__":
    main()
