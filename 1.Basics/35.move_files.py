import os
source = "copiedtext.txt"
destinations = "D:\\Python Code\\Bro Code\\temporary\\copiedtext.txt"

try:
    if(os.path.exists(destinations)):
        print("Already exists")
    else:
        os.replace(source, destinations)
        print(source+" was moved")
except Exception as e:
    print(source, e)