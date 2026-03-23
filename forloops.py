## For loop syntax
for i in range (0,5):
    print (i)

## For Loop with Lists
l = [1, 4, 6, 234, 6, 764]
for i in l:
    print(i)

## For Loop with Tuples
t = (6, 231, 75, 122)
for i in t:
    print(i)

## For Loop with Strings
s = "Swetank"
for i in s:
    print(i)

## For loop with else
l= [1,7,8] 

for item in l:
    print(item)

else:
    print("done") # this is printed when the loop exhausts!

## For loop in brk and continue
for i in range(100):
    if(i == 34):
        break # Exit the loop right now
    print(i)

for i in range(100):
    if(i == 34):
        continue # Skip this iteration
    print(i)    

## pass statement for loop
for i in range(645):
    pass

i = 0
while(i<45):
    print(i)
    i += 1