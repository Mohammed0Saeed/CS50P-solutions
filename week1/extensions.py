# prompt the user to enter the file name
file_name = input("File name: ").replace(" ", "").lower()

# check if the file is image or application
if file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
    print("image/jpeg")
elif file_name.endswith(".gif"):
    print("image/gif")
elif file_name.endswith(".png"):
    print("image/png")
elif file_name.endswith(".pdf"):
    print("application/pdf")
elif file_name.endswith(".zip"):
    print("application/zip")
elif file_name.endswith(".txt"):
    print("text/" + file_name.replace(".txt", ""))
else:
    print("application/octet-stream")
