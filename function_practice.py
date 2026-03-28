## Even Numbers 
def is_even(n):
      return n % 2 == 0
n = int(input("Enter a number: "))
print("is_even:", is_even(n))


## Prime Numbers
def is_prime(n):
    if n<=1:
      return False
    for i in range(2, int(n**0.5) + 1):
       if n % i == 0:
          return False
    return True
n = int(input("Enter a number: "))
print("is_prime:", is_prime(n))


## Fibonacci Numbers
def fibonacci(n):
    fib = []
    a, b = 0, 1
    for _ in range(n):
        fib.append(a)
        a, b = b, a + b
    return fib
n = int(input("Enter a number: "))
print("fibonacci:", fibonacci(n))

## Palindrome Number
def is_palindrome(s):
    return s == s[::-1]
n = str(input("Enter: "))
print("is_palindrome:", is_palindrome(n))