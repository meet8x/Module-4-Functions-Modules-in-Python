
import math

try:
    val1 = int(input("Enter a Number: "))
    if val1 <= 0:
        print("Please enter a number greater than 0 for square root and logarithm.")
    else:
        sqrt = math.sqrt(val1)
        nlog = math.log(val1)
        sinval = math.sin(val1)
        print("square root:",sqrt)
        print("Logaritham",nlog)
        print("Sine",sinval)

except ValueError:
    print("Invalid input. Please enter a valid number.")



