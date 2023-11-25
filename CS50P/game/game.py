import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

lotto = random.randint(1,level)

while True:
    try:
        guess = int(input("Guess: "))
        if lotto == guess:
            print("Just right!")
            break
        elif lotto > guess:
            print("Too small!")
        elif lotto < guess:
            print("Too large!")
    except ValueError:
        pass

