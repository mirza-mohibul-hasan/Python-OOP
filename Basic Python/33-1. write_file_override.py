newText = "Mirza Refat\nUndegrad student"
with open('text.txt', 'w') as file: #by default open is in read(r) mode, we have to change it to write 'w', 'w' override the file
    file.write(newText)