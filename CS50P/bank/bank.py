answer = input("Greeting: ")
if answer.strip().lower().startswith("hello"):
    print("$0")
elif answer.strip().lower().startswith("h"):
    print("$20")
else:
    print ("$100")



