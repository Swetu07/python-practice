## List Comprehension

# Without comprehension
squares = []
for x in range(6):
    squares.append(x ** 2)

# With comprehension
squares = [x ** 2 for x in range(6)]
# [0, 1, 4, 9, 16, 25]

# With condition (filter)
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]

## Dictionary Comprehension

# Build a dict from a list
words = ["apple", "banana", "kiwi"]
lengths = {word: len(word) for word in words}
# {'apple': 5, 'banana': 6, 'kiwi': 4}

##  Set Comprehension

# Automatically removes duplicates
nums = [1, 2, 2, 3, 3, 3]
unique_squares = {x ** 2 for x in nums}
# {1, 4, 9}

## Generator Expression

# Doesn't store all values in memory at once
gen = (x ** 2 for x in range(1_000_000))

print(next(gen))  # 0
print(next(gen))  # 1

# Works great with functions like sum(), max()
total = sum(x ** 2 for x in range(100))