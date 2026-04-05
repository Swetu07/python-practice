 ## Class and objects
class Person:
    name = "Swetank"
    age = 21
    aim = "Software developer"

#a = Person
#print(a.name)
#print(a.age)
#print(a.aim)

## Self keyword
    def info(self):
        print(f"{self.name} is a {self.aim}")


a = Person()
a.name = "Koffee"
a.aim = "CA"


a.info() 
