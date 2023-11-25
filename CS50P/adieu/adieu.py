import inflect
p = inflect.engine()
nlist = []
mytext = "Adieu, adieu, to "
mycount = 0
while True:
    try:
        nam = input("Name: ")
        nlist.append(nam)

    except EOFError:
        print()
        break

print (f"{mytext}" + p.join(nlist))
