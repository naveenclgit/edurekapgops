def main():
    answer = input("Greeting: ")
    myval = value(answer)
    print(f"${myval}")

def value(greeting):
    if greeting.strip().lower().startswith("hello"):
        return 0
    elif greeting.strip().lower().startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()






