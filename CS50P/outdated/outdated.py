monthst = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

#loop
while True:
    #user input
    ydate = input("Date: ")
    try:
        m,d,y = ydate.split("/")
        mn = int(m)
        dt = int(d)
        yr = int(y)
        if (mn >= 1 and mn <=12) and (dt >= 1 and dt <= 31):
            break

    except:
        try:
            m,d,y = ydate.split(" ")
            try:
                dt = int(d)
            except:
                dt = int(d.replace(",",""))
                yr = int(y)
                mnth = monthst.index(m,0,11)
                mn = int(mnth + 1)
                if (mn >= 1 and mn <=12) and (dt >= 1 and dt <= 31):
                    break
            else:
                pass 
        except:
                pass

print (f"{yr}-{mn:02}-{dt:02}")


