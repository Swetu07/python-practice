name = "Swetank"

nameshort = name[0:3] # start from index 0 all the way till 3 (excluding 3)
print(nameshort)
character1 = name[1]
print(character1)

# Negative slicing
name = "Swetank"

print(name[0:3])

print(name[-4: -1])
print(name[1:4])

print(name[:4]) # is same as print(name[0:4])
print(name[1:]) # is same as print(name[1:5])
print(name[1:5])

# string function
name = "swetank"

print(len(name))
print(name.endswith("ank"))
print(name.startswith("sw"))
print(name.capitalize())

# escape sequence
a = 'Swet is a good boy\nbut not a bad \'boy\''
print(a)