import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    workhrs = ""
    startsec = ""
    endsec = ""

    if time := re.search(
        r"(^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$)",
        s,
    ):
        myhours = time.groups()
        # return myhours
        if int(myhours[2]) > 12 or int(myhours[6]) > 12:
            raise ValueError

        if (myhours[3] and myhours[7]) and (int(myhours[3]) > 59 or int(myhours[7]) > 59):
            raise ValueError

        if myhours[3]:
            startsec = myhours[3]
        else:
            startsec = "00"

        if myhours[7]:
            endsec = myhours[7]
        else:
            endsec = "00"

        if myhours[4] == "AM" and int(myhours[2]) != 12:
            workhrs = str(f"{int(myhours[2]):02}") + ":" + startsec
        elif myhours[4] == "AM" and int(myhours[2]) == 12:
            workhrs = "00" + ":" + startsec
        elif myhours[4] == "PM" and int(myhours[2]) != 12:
            workhrs = str(int(myhours[2]) + 12) + ":" + startsec
        elif myhours[4] == "PM" and int(myhours[2]) == 12:
            workhrs = "12" + ":" + startsec


        if myhours[8] == "AM" and int(myhours[6]) != 12:
            workhrs = workhrs + " to " + str(f"{int(myhours[6]):02}") + ":" + endsec
        elif myhours[8] == "AM" and int(myhours[6]) == 12 :
            workhrs = workhrs + " to " + "00" + ":" + endsec
        elif myhours[8] == "PM" and int(myhours[6]) != 12 :
            workhrs = workhrs + " to " + str(int(myhours[6]) + 12) + ":" + endsec
        elif myhours[8] == "PM" and int(myhours[6]) == 12 :
            workhrs = workhrs + " to " + "12" + ":" + endsec


    else:
        raise ValueError
    return workhrs


if __name__ == "__main__":
    main()
