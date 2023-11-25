
mytext = input("Input: ")
twt = ""

for l in mytext:
    if l.lower() in ["a","e","i","o","u"]:
        twt = twt
        #print(f"{twt}")
    else:
        twt = twt + l

print (f"Output: {twt}")



