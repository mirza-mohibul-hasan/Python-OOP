food = ["pizza", "Makhon", "Anda Curry", "burger", "meat"]

print("\n########## append ########")
food.append("pudding")
for f in food:
    print(f)

print("\n########## remove ########")
food.remove("burger")
for f in food:
    print(f)

print("\n########## pop ########")
food.pop()
for f in food:
    print(f)

print("\n########## insert ########")
food.insert(1, "Rosgolla")
for f in food:
    print(f)

print("\n########## sort ########")
food.sort()
for f in food:
    print(f)

print("\n########## Clear ########")
food.clear()
for f in food:
    print(f)