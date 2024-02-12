newText = "\nAlso a full-stack MERN developer\nCurently in 3rd year 2nd semester"
with open('text.txt', 'a') as file: #by default open is in read(r) mode, we have to change it to write 'a', 'a' append the file
    file.write(newText)