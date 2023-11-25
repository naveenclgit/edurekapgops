def main():
    mytext = input("Input: ")
    twt = shorten(mytext)
    print (f"Output: {twt}")

def shorten(word):
    twt = ""
    for l in word:
        if l.lower() in ["a","e","i","o","u"]:
            twt = twt
        else:
            twt = twt + l
    return twt

if __name__ == "__main__":
    main()
