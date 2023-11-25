def main():
    inarg = input()
    parg = convert(inarg)
    print(f"{parg}")

def convert(inarg):
    outarga = inarg.replace(":(","🙁")
    outarg = outarga.replace(":)","🙂")
    return outarg
main()