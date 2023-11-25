answer = input("File name: ").strip().lower().split(".")[-1]

match answer:
    case "gif" |  "jpeg" | "png":
        print(f"image/{answer} ")
    case "jpg":
        print("image/jpeg")
    case "pdf" |  "zip":
        print(f"application/{answer} ")
    case  "txt" :
        print("text/plain")
    case _:
        print("application/octet-stream")
