## DICT SYNTAX
d = {} # Empty dictionary
marks = {
    "Swet": 100,
    "Swetank": 56,
    "Ansh": 23
}

## DICT METHODS
# print(marks, type(marks))
print(marks["Swet"])


marks = {
    "Swet": 100,
    "Swetank": 56,
    "Ansh": 23,
    0: "Jeevan"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Swet": 99, "Koffee": 100})
# print(marks)

print(marks.get("Swet2")) # Prints None
print(marks["Swet2"]) # Returns an error