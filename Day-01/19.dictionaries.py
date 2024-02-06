# dictionary =  a collection of {key:value} pairs, unordered and changeable. No duplicates. Support hasing

capitals = {"USA":"Washington DC", "UK":"London", "India":"New Delhi", "Russia":"Moscow"}

print("\nNormal Ways to access: ")
print("**************************")
print(capitals)
print(capitals["UK"])

print("\nBest Ways to access: ")
print("**************************")
print(capitals.get("UK"))
print(capitals.get("KSA"))

print("\nUpdate: ")
print("**************************")
capitals.update({"Germany":"Berlin"})
print(capitals)

print("\nPrint Keys: ")
print("**************************")
print(capitals.keys())

print("\nPrint Values: ")
print("**************************")
print(capitals.values())

print("\nPrint Values: ")
print("**************************")
print(capitals.items())

print("\nPrint using loop: ")
print("**************************")

for key, value in capitals.items():
    print(key,":", value)

print("\nPop: ")
print("**************************")
capitals.pop("India")
print(capitals)

print("\nClear: ")
print("**************************")
capitals.clear()
print(capitals)