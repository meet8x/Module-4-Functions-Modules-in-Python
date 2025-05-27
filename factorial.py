
def facto(val):
    if val < 2:
        return 1
    else:
        return val * (facto(val - 1))

ans1 = facto(5)
print("Factorial of 5 is:",ans1)

