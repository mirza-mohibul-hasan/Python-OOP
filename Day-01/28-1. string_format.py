
animal = "cow"
item = "moon"

#Normal Way
print("The "+animal+" jumped over the "+item)
#String format Way
print("The {} jumped over the {}".format(animal, item))
print("The {1} jumped over the {0}".format(animal, item)) #positonal argument
print("The {1} jumped over the {1}".format(animal, item)) #positonal argument
print("The {animalkw} jumped over the {itemkw}".format(animalkw=animal, itemkw=item)) #keyword argument