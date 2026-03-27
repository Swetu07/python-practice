# a = int(input("Enter your number: "))
# b = int(input("Enter your number: "))
# c = int(input("Enter your number: "))
 
# average = (a + b + c)/3
# print(average)

# a = int(input("Enter your number: "))
# b = int(input("Enter your number: "))
# c = int(input("Enter your number: "))
 
# average = (a + b + c)/3
# print(average)

# Function Definition
#def avg():
#    a = int(input("Enter your number: "))
#    b = int(input("Enter your number: "))
#    c = int(input("Enter your number: "))
#    
#    average = (a + b + c)/3
#    print(average)
#
#
#avg() # Function Call
#print("Thank you!")
#avg()
#print("Thank you!")
#avg()
#print("Thank you!")
#avg()
#avg()


def goodDay(name, ending):
    print("Good Day, " + name)
    print(ending)
    return "ok"

a = goodDay("Swet", "Thank you") 
print(a)


def goodDay(name, ending="Thank you"):
    print(f"Good Day, {name}")
    print(ending)

goodDay("Swetank", "Thanks")
goodDay("Rohan")