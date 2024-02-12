# sliceing =  create a substring by extracting elements from another string
#indexing[] or slice()
# [start_index:stop_index:step]
print("\n######## using Indexing ######")
name = "Mohibul Hasan"

# first_name = name[0:7] # last index is inclusive
first_name = name[:7] # last index is inclusive
print(first_name)

# last_name = name[8:13] # last index is inclusive
last_name = name[8:] # last index is inclusive
print(last_name)

# funky_name = name[0:13:3] # last index is inclusive
funky_name = name[::3] # last index is inclusive
print(funky_name)

reverse_name = name[::-1]
print(reverse_name)

print("\n######## using Slicing ######")
# [start_index , stop_index , step]

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7, -4)

print(website1[slice])
print(website2[slice])
