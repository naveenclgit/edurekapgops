#loop
while True:
    #user input
    gas = input("Fraction: ")
    try:
        #split the input
        C,T = gas.split("/")
        #int'ize it
        c = int(C)
        t = int(T)
        if t >= c:
            #calc ratio
            pa = c / t
            #check if less than 1  then prnt E and exit
            if pa <= 1:
                break
            if c == 0:
                print("E")
                break
        else:
            raise ValueError
    except (ValueError, ZeroDivisionError):
        pass
if pa > .1 and pa < .99:
    pc = int(round(pa,2) * 100)
    print(f"{pc}%")
elif pa >= .99:
    print("F")
elif pa < .1:
    print("E")

