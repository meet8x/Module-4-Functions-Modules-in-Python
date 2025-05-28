
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n < 2:
        return 1
    else:
        return n * (factorial(n - 1))

try:
    num = int(input("Enter a number: "))
    result = factorial(num)
    print(f"Factorial of {num} is: {result}")
except ValueError:
    print("Please enter a valid integer.")

