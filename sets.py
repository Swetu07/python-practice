## Sets
e = set() # Dont use s = {} as it will create an empty dictionary
s = {1, 5, 32, 54,5, 5, 5} 

print(s)

## Sets methoods
s = {1, 5, 32, 54,5, 5, 5, "swet"}

print(s, type(s))

s.add(566)
print(s, type(s))
s.remove(1)
print(s, type(s))

## union and intersection
s1 = {1, 45, 6, 78}  
s2 = {7, 8, 1, 78}

print(s1.union(s2))
print(s1.intersection(s2))
