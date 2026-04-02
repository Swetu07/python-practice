friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]

print(friends[0])
friends[0] = "Grapes" # Unlike Strings lists are mutable

print(friends[0])
print(friends[1:4])

## list methods
friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
print(friends)
friends.append("Harry")
print(friends)

l1 = [1, 34,62, 2, 6, 11]
# l1.sort()
# l1.reverse()
# l1.insert(2, 333333) # Insert 333333 such that its index in the list is 3
value = l1.pop(3)
print(value)
print(l1)

## practice

marks = []

# Input marks for 5 subjects
for i in range(5):
    m = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(m)

# Initialize
max_marks = marks[0]
min_marks = marks[0]
total = 0

# Loop to find max, min, sum
for m in marks:
    if m > max_marks:
        max_marks = m
    if m < min_marks:
        min_marks = m
    total += m

average = total / len(marks)

print("\nMarks:", marks)
print("Maximum:", max_marks)
print("Minimum:", min_marks)
print("Sum:", total)
print("Average:", average)