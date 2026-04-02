import json

student = {"name": "Swetank", "marks": 85}
json_text = json.dumps(student)
print(json_text)
print(type(json_text))