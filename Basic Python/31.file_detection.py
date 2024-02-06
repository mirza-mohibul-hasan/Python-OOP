import os
path = ".\\text.txt"

# Check if the location exists or not
if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("it's a file")
    elif os.path.isdir(path):
        print("it's a directory")
else:
    print("Doesn't exists")