name = "mohibul Refat"

print('\n'+"*********Length********")
print(len(name))

print('\n'+"*********Index of a character works********")
print(name.find("R"))

print('\n'+"*********Capitalized means First char of word is Capital********")
print(name.capitalize())

print('\n'+"*********Uppercase means all char of word is Capital********")
print(name.upper())

print('\n'+"*********lower means all char of word is Capital********")
print(name.lower())

print('\n'+"*********isdigit() means they are number or not********")
print(name.isdigit())

number = "1234"
print(number.isdigit())

print('\n'+"*********isalpha() means they are alphabetical or not********")
print(name.isalpha())

number = "SureShot"
print(number.isalpha())

print('\n'+"*********count("") means count how many********")
print(name.count('f'))

print('\n'+"*********replace() means count how many********")
print(name.replace('Refat', 'hasan'))

print('\n'+"*********print multiple times********")
print(name*3)