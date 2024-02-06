import os
path = "copiedtext.txt"
try:
    os.remove(path) # remember os.rmdir(path) & shutill.rmtree(path)
except Exception as e:
    print(e)