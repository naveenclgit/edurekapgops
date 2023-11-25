
camelCase = input("camelCase: ")
snake_case = ""

for l in camelCase:
    if l.isupper():
        snake_case = snake_case + "_" + l.lower()
    else:
        snake_case = snake_case + l

print (f"{snake_case}")



