try:
    with open('text.txt') as file: # for same directory it's also works
        print(file.read())
except Exception as e:
    print(e)