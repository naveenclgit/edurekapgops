# reference  me50 / users / naveenclgit / cs50 / problems / 2023 / x / credit
import re


# regular expressions to validate user input using Python’s re module
def getcardnumcheck(cnumber):
    cnleng = len(cnumber)
    # checking if card number has invalid chars
    if not re.match("^[0-9]*$", cnumber):
        return 0
    else:
        return 1


# Check card type
def getcardtype(cnumber):
    if cnumber[0] == '4' and (len(cnumber) == 16 or len(cnumber) == 13):
        return "VISA"
    elif cnumber[0] == '5' and int(cnumber[1]) in range(1, 6):
        return "MASTERCARD"
    elif cnumber[0] == '3' and (cnumber[1] == '4' or cnumber[1] == '7'):
        return "AMEX"
    else:
        return "INVALID"


# applying Luhn’s Algorithm
def iscardvalid(cnumber):
    sum = 0
    cnleng = len(cnumber)
    for i in range(cnleng - 2, -1, -2):
        if int(cnumber[i]) * 2 > 9:
            sum += (int(cnumber[i]) * 2) - 9
        else:
            sum += int(cnumber[i]) * 2
    for i in range(cnleng - 1, -1, -2):
        sum += int(cnumber[i])
    if sum % 10 == 0:
        return 1
    else:
        return 0


vald = "INVALID"
cnumber = ""
while True:
    # Get card number and basic validation
    cnumber = input("Number: ")
    if getcardnumcheck(cnumber) == 1 or getcardnumcheck(cnumber) == 2:
        break
# Validate card number
if getcardnumcheck(cnumber) == 1:
    vald = "VALID"
elif getcardnumcheck(cnumber) == 2:
    print(vald)
# if card is valid proceed to procees other checks
if vald == "VALID":
    crdvld = iscardvalid(cnumber)
    if crdvld == 1:
        crdtype = getcardtype(cnumber)
        print(crdtype)
    else:
        print("INVALID")
