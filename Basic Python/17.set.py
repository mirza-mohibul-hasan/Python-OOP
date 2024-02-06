# set is a collection which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup"}

for x in utensils:
    print(x)

utensils.add("napkin")
utensils.remove("spoon")
print(utensils)

# utensils.update(dishes)
# print(utensils)

dinner_table = utensils.union(dishes)
print(dinner_table)

utensils.add("cup")
print(dishes.difference(utensils))