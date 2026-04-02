import json

student = {"name": "Swetank", "marks": 85}

# Dict → JSON string
json_text = json.dumps(student)
print(json_text)
print(type(json_text))

# JSON string → Dict (REVERSE)
back_to_dict = json.loads(json_text)
print(back_to_dict)
print(type(back_to_dict))

# Save to file
with open("student.json", "w") as f:
    json.dump(student, f)

# Read from file
with open("student.json", "r") as f:
    loaded = json.load(f)

print(loaded)
print(type(loaded))