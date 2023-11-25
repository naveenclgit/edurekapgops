import random

def main():
    tscore = 0
    mycnt = 0
    level = get_level()
    while mycnt < 10:
        a,b = generate_integer(level)
        if game_try(a,b):
            tscore = tscore + 1
        else:
            print(f"{a} + {b} = {a+b}")
        mycnt = mycnt + 1
    print(f"Score: {tscore}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level >= 1 and level <=3:
                break
        except ValueError:
            pass
    return level


def generate_integer(level):
    if level == 1:
        a = random.randint(0,9)
        b = random.randint(0,9)
    elif level == 2:
        a = random.randint(10,99)
        b = random.randint(10,99)
    elif level == 3:
        a = random.randint(100,999)
        b = random.randint(100,999)
    return a,b

def game_try(a,b):
    mytry = 1
    uscore = 0
    while mytry <= 3:
        try:
            answer = int(input(f"{a} + {b} = "))
            if answer == (a + b):
                uscore = 1
                return True
            else:
                mytry += 1
                print ("EEE")
        except ValueError:
            mytry += 1
            print ("EEE")
    return False

if __name__ == "__main__":
    main()
