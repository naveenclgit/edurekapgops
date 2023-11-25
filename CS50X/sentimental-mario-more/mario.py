from cs50 import get_int

# get the height and if not between 1 and 8 keep looping
while True:
    height = get_int("Height: ")
    if height > 0 and height < 9:
        break

# print # in loop, first space and hash for left side
for cnt in range(1, height + 1):
    print(" " * (height - cnt) + "#" * cnt, end="")
# then pring 2 spaces
    print("  ", end="")
# then print right hash
    print("#" * cnt)
