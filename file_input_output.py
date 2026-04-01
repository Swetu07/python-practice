## files read
'''
a = "a very long string with emails"

emails = []
3 seconds
'''

f = open("python/file.txt", "r")
data = f.read()
print(data)
f.close()

## file write
st = "Hey Swetank you are amazing"

f = open("python/myfile.txt", "w")

f.write(st)

f.close()

## more function
f = open("python/file.txt")

# lines = f.readlines()
# print(lines, type(lines))

# line1 = f.readline()
# print(line1, type(line1))

# line2 = f.readline()
# print(line2, type(line2))

# line3 = f.readline()
# print(line3, type(line3))

# line4 = f.readline()
# print(line4, type(line4))

# line5 = f.readline()
# print(line5 =="")
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

f.close()

## append
st = "Hey Swetank you are amazing"

f = open("python/myfile.txt", "a")

f.write(st)

f.close()

## with
f = open("python/file.txt")
print(f.read())
f.close()

# The same can be written using with statement like this:
with open("python/file.txt") as f:
    print(f.read())

# You dont have to explicitly close the file

## files are in txt
